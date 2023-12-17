from rest_framework import serializers
from django.contrib.auth import update_session_auth_hash
from .models import CATEGORY,ARTIST, PRODUCT, IMAGE, Account,LINK, AccountManager, GALLERY
# from .models import CATEGORY,ARTIST, PRODUCT, IMAGE, USER, Account, AccountManager

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CATEGORY
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARTIST
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRODUCT
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LINK
        fields = '__all__'
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMAGE
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = GALLERY
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = USER
#         fields = (
#             "id",
#             "name",
#             "email",
#             "password",
#             "regist_date"
#         )


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('id', 'username', 'email', 'password' )

    def create(self, validated_date):
        return Account.objects.create_user(request_data=validated_date)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance
    
class MailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('toAddress', 'product',  )
