from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True) #we are using nested serializer to get the category details in the product serializer and we are making it read only because we dont want to create or update the category from the product serializer
    
    class Meta:
        model = Product
        fields = '__all__'