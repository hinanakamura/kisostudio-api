from django.contrib import admin

# from .models import CATEGORY, PRODUCT, IMAGE, USER
from .models import CATEGORY, PRODUCT, IMAGE,Account
class ImageInline(admin.StackedInline):
    model = IMAGE
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(PRODUCT, ProductAdmin)
admin.site.register(CATEGORY)
admin.site.register(Account)
# admin.site.register(USER)