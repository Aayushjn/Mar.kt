from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'seller'

urlpatterns = [
    path('dashboard/', views.display_seller_dash, name="dashboard"),
    path('dashboard/listings', views.display_seller_list, name="listings"),
    path('dashboard/item', views.display_seller_item, name="item"),
    path('dashboard/mod', views.display_seller_mod, name="mod"),
   
]
