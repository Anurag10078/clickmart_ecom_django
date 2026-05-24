from django.urls import path
from users import views as UserViews
from products import views as ProductViews

urlpatterns = [
    
 #    path('register/',UserViews.RegisterView.as_view())
 #   path('token/',)
 
    #catogries api
    path('categories/',ProductViews.CatogeryListView.as_view()),
    
    #products api
    path('products/',ProductViews.ProductListView.as_view()),
    
    #product details api
    path('products/<int:id>/',ProductViews.ProductDetailView.as_view()),
]