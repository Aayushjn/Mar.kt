from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'buyer'

urlpatterns = [
    path('dashboard/', views.display_buyer_dash, name="dashboard"),
    path('dashboard/category', views.display_buyer_cat, name="category"),
]