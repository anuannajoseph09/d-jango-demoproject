"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views

app_name="shop"
urlpatterns = [
    path('',views.allcategories,name="categories"),
    path('products/<int:p>',views.allproducts,name="products"),
    path('detail/<int:i>', views.detail, name="detail"),
    path('login',views.user_login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.user_logout,name="logout"),
    path('orders',views.user_orders,name="orders"),
    path('addproduct',views.add_product,name="addproduct"),
    path('addcat',views.add_cat,name="addcat"),
    path('add_stock/<int:i>',views.add_stock,name="add_stock"),

]




