from django.contrib import admin
from django.urls import path
from . import views
app_name = 'pages'
app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
