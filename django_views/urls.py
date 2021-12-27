from django import urls
from django.contrib import admin
from  django.urls import path
from web_transfer import views


urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    
    ]

