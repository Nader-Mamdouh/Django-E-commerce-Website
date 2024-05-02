from django.urls import path
from ecommerce_app import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'),
    path('watches/', views.watches, name='watches'),
    path('product/<int:pk>', views.product, name='product'),
]
