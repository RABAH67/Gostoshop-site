from django.urls import path 
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('detail/<slug:slug>/add_to_cart/',views.add_to_cart,name='add_to_cart'),
	path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
	path('singup/',views.CreateUserViews.as_view(),name='singup'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]