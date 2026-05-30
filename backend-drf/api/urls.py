from django.urls import path
from users import views as UserViews 
from products import views as ProductViews
from cart import views as CartViews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    # user registration api
    path('register/',UserViews.RegisterView.as_view()),
    #user login api
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #it wil give us the access tokens 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#it will be given by refresh token 
    #to get the user profile api
    path('profile/',UserViews.ProfileView.as_view()),
 
    #catogries api
    path('categories/',ProductViews.CategoryListView.as_view()),
    
    #products api
    path('products/',ProductViews.ProductListView.as_view()),
    
    #product details api
    path('products/<int:id>/',ProductViews.ProductDetailView.as_view()),
    
    #Carts API
    path('carts/',CartViews.CartListView.as_view()),
    
    path('cart/add/',CartViews.AddToCartView.as_view()),
    
    path('cart/item/<int:item_id>/',CartViews.ManageCartItemView.as_view()),
    
    
]