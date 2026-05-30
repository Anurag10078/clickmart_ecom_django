from rest_framework import serializers
from .models import Cart,CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name =serializers.CharField(source="product.name")
    price = serializers.DecimalField(source="product.price", max_digits=6, decimal_places=2)
    tax_percent = serializers.DecimalField(source="product.tax_percentage", max_digits=10, decimal_places=2)
    class Meta:
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True) #this is for nested serialization, we want to show the items in the cart along with the cart details
    subtotal = serializers.DecimalField(max_digits=6, decimal_places=2)
    grand_total = serializers.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        model = Cart
        fields = "__all__"
    