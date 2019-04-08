from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = 'seller'

urlpatterns = [
    path('dashboard/', views.display_seller_dash, name="dashboard"),
    path(r'dashboard/item/edit/(?P<item_id>\d+)/$', views.display_seller_mod, name="mod"),
    # url(r'^dashboard/item/(?P<item_id>\d+)/$', views.display_seller_mod, name="mod"),
    url(r'^dashboard/listings/(?P<category_id>\d+)/$', views.display_seller_list, name="listings"),
    url(r'^dashboard/item/(?P<item_id>\d+)/$', views.display_seller_item, name="item"),


]
