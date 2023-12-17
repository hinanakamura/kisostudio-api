from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.db import transaction
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash, authenticate
from rest_framework import viewsets, authentication, permissions, generics, status, serializers
# from .serializers import CategorySerializer, ProductSerializer, ImageSerializer, UserSerializer, AccountSerializer
from .serializers import CategorySerializer,  ArtistSerializer,ProductSerializer, ImageSerializer, GallerySerializer,LinkSerializer, AccountSerializer
# from .models import CATEGORY,  ARTIST,PRODUCT, IMAGE, USER, Account, AccountManager
from .models import CATEGORY, ARTIST,PRODUCT, IMAGE, Account,GALLERY,LINK, AccountManager
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from django.core.mail import BadHeaderError, send_mail

def index(request):
    latest_product_list = PRODUCT.objects.order_by("-pub_date")[:3]
    context = {"latest_product_list": latest_product_list}
    return render(request, "ec/index.html", context)

def collections(request):
    products = PRODUCT.objects.order_by("-pub_date")
    context = {"products": products}
    return render(request, "ec/collections.html", context)

def send_email(request):
    subject = request.POST.getlist("subject", "")
    message = request.POST.getlist("message", "")
    payment_intent = request.GET.get("payment_id")
    to_email = request.GET.get("to_email")
    name = request.GET.get("name")
    shipping = request.GET.get("shipping")
    price = request.GET.get("price")
    if to_email:
        try:
            send_mail("[KISO STUDIO]ご注文完了のお知らせ", name+"様 \n\nご購入が完了しました。商品発送までお待ちください。\n\n購入金額:"+price+"円\n\nお届け先：〒 "+shipping+"\n\n決済ID："+payment_intent+"\n\nご不明点はstaff@kiso.studioにご連絡ください。", "staff@kiso.studio", [to_email])
            send_mail("[KISO STUDIO]注文受領のお知らせ", name+"様から \n\n注文を受領しました。商品を発送してください。\n\n購入金額:"+price+"円\n\nお届け先：〒 "+shipping+"\n\nメールアドレス："+to_email+"\n\n決済ID："+payment_intent+"\n\n", "staff@kiso.studio", ["staff@kiso.studio"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("/contact/thanks/")
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse("Make sure all fields are entered and valid.")
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = CATEGORY.objects.all()
    def get_queryset(self):
        if self.queryset is not None:
            return CATEGORY.objects.filter( Q(id = self.request.query_params.get('id')))

class ArtistViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = ArtistSerializer
    queryset = ARTIST.objects.all()
    def get_queryset(self):
        if self.queryset is not None:
            return ARTIST.objects.filter( Q(artist_id = self.request.query_params.get('artist_id'))| Q(id = self.request.query_params.get('id')))
        else:
            return ARTIST.objects.all()
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = PRODUCT.objects.all()
    def get_queryset(self):
        if self.queryset is not None:
            return PRODUCT.objects.filter( Q(category = self.request.query_params.get('category'))| Q(id = self.request.query_params.get('id'))| Q(artist = self.request.query_params.get('artist_id')))
        else:
            return PRODUCT.objects.all()
        
# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = [HasAPIKey | IsAuthenticated]
#     serializer_class = UserSerializer
#     queryset = USER.objects.all()
#     def post(self, request, *args, **kwargs):
#         return Response({'result':True})

class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = ImageSerializer
    queryset = IMAGE.objects.all()
    def get_queryset(self):
            return IMAGE.objects.filter( Q(product = self.request.query_params.get('product')))

class GalleryViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = GallerySerializer
    queryset = GALLERY.objects.all()
    def get_queryset(self):
            return GALLERY.objects.filter( Q(artist = self.request.query_params.get('artist')))
    
class LinkViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    serializer_class = LinkSerializer
    queryset = LINK.objects.all()
    def get_queryset(self):
            return LINK.objects.filter( Q(artist = self.request.query_params.get('artist')))

class AuthRegister(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @transaction.atomic
    def post(self, request, format = None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AuthInfoGetView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, fromat=None):
        return Response(data={
            'username': request.user.username,
            'email': request.user.email,
            'profile': request.user.profile,
        },
        status=status.HTTP_200_OK)
    
class AuthInfoUpdateView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    lookup_field = 'email'
    queryset = Account.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Account.DoesNotExist:
            raise Http404


class AuthInfoDeleteView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AccountSerializer
    lookup_field = 'email'
    queryset = Account.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except Account.DoesNotExist:
            raise Http404

