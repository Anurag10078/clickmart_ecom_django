from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from .models import Cart,CartItem
from .serializer import CartSerializer

# Create your views here.
class CartListView(APIView):#here we want more control 
    permission_classes = [IsAuthenticated]
    def get(self,request):
        cart, created = Cart.objects.get_or_create(user=request.user) #means get the cart or create the cart 
        # if created: #crated is boolean
        #     print('cart created')
        serializer = CartSerializer(cart)
        return Response(serializer.data)
 
    
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated] #only authenticated users can add to cart
    
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1) #default quantity is 1 if not provided
        
        if not product_id:
            return Response({'error': 'Product ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        product = get_object_or_404(Product, id=product_id, is_active=True)
        
        cart, _ = Cart.objects.get_or_create(user=request.user)
        
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if not created:
            item.quantity += quantity
            item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ManageCartItemView(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self,request,item_id):
            
        
        if 'change' not in request.data: #chabge should be in request data and it should be either +1 or -1s
            return Response({'error':'Change is required'},status=status.HTTP_400_BAD_REQUEST)
        
        change = int(request.data.get('change'))
        
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        product = item.product
        
        if change>0:
            if item.quantity + change > product.stock:
                return Response({'error':'Not enough stock'},status=status.HTTP_400_BAD_REQUEST)
        
        new_qty = item.quantity + change
        
        if new_qty <= 0:
            item.delete()
            return Response({'message':'Item removed from cart'},status=status.HTTP_200_OK)
        
        item.quantity = new_qty
        item.save()
        serializer = CartSerializer(item.cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self,request,item_id):
        item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
        item.delete()
        return Response({'message':'Item removed from cart'},status=status.HTTP_200_OK)