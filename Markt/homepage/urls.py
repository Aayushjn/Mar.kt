from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.display_home, name="home"),
    path('login/', views.display_login, name="login"),
    path('signup/', views.display_signup, name="signup"),
    path('dashboard/',views.display_dash_home, name="dash_home"),
]
