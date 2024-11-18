"""
URL configuration for movie project.

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
from app1 import views
app_name="app1"
urlpatterns = [
    # path('',views.home,name="home"),
    #class calling
    path('',views.Home.as_view(),name="home"),
    # path('add',views.addmovie,name="add"),
    # path('add1',views.addmovie1,name="add1"),
    path('add1',views.Addmovie.as_view(),name="add1"),
    # path('detail/<int:i>', views.detail, name="detail"),
    path('detail/<int:pk>',views.Detail.as_view(),name="detail"),

    # path('edit/<int:a>',views.edit,name="edit"),
    path('edit/<int:pk>',views.Edit.as_view(),name="edit"),
    # path('delete/<int:p>',views.delete,name="delete"),
    path('delete/<int:pk>',views.Delete.as_view(),name="delete"),
]
