from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('ShopNew/', views.ShopPage,name='ShopNew'),
    path('detail/<slug:slug>', views.single_product,name='detail'),
]