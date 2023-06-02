from django.db import models

class CATEGORY(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class PRODUCT(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
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
