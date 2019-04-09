from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'buyer'

urlpatterns = [
    path('dashboard/', views.display_buyer_dash, name="dashboard"),
    url(r'^dashboard/category/(?P<category_id>\d+)/$', views.display_buyer_cat, name="category"),
    url(r'^dashboard/item/(?P<item_id>\d+)/$', views.display_buyer_item, name="item"),
]
