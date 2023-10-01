from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, _user_has_perm
)
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CATEGORY(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class PRODUCT(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True)
    stripe_id = models.CharField(max_length=200)
    stock_count = models.IntegerField(default=1)
    thumbnail = models.FileField(null=True)
    category = models.ForeignKey(CATEGORY, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.product_name

class IMAGE(models.Model):
    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    image = models.FileField(null=True)
    order = models.IntegerField(default=1)

class AccountManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('Users must have an email address.')
        
        profile = ""
        if request_data.get('profile'):
            profile = request_data['profile']

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            last_login=now,
            date_joined=now,
            profile=profile
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password,
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField( max_length=30,unique=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True)
    profile = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def user_has_perm(user,perm,obj):
        return _user_has_perm(user,perm,obj)
    
    def has_perm(self,perm,obj=None):
        return _user_has_perm(self, perm, obj=obj)
    
    def has_module_perms(self,app_label):
        return self.is_admin
    
    def get_short_name(self):
        return self.first_name
    
    @property
    def is_superuser(self):
        return self.is_admin
    
    
    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'

