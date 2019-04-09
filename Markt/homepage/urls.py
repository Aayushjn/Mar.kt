from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.display_home, name="home"),
    path('login/', views.display_login, name="login"),
    path('signup/', views.display_signup, name="signup"),
    path('dashboard/', views.display_dash_home, name="dash_home"),
    path('mailbox/', views.display_mail_home, name="mail_home"),
    path('mailbox/mailview', views.display_mail, name="mail_view"),

]

if settings.DEBUG:
    urlpatterns += static(settings.PRODUCTS_URL, document_root=settings.PRODUCTS_ROOT)
