from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer, ImageSerializer
from .models import CATEGORY, PRODUCT, IMAGE

def index(request):
    latest_product_list = PRODUCT.objects.order_by("-pub_date")[:3]
    context = {"latest_product_list": latest_product_list}
    return render(request, "ec/index.html", context)

def collections(request):
    products = PRODUCT.objects.order_by("-pub_date")
    context = {"products": products}
    return render(request, "ec/collections.html", context)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CATEGORY.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = PRODUCT.objects.all()
    def get_queryset(self):
        if self.queryset is not None:
            return PRODUCT.objects.filter( Q(category = self.request.query_params.get('category'))| Q(id = self.request.query_params.get('id')))
        else:
            return PRODUCT.objects.all()
         

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = IMAGE.objects.all()