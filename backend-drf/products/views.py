from django.shortcuts import render
from rest_framework import generics
from .models import Category,Product
from .serializers import CategorySerializer , ProductSerializer

# Create your views here.
class CatogeryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    lookup_field = 'id' #we are using id as the lookup field to get the product details