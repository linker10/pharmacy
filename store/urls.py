from django.contrib import admin
from django.urls import path
from . import views
from .views import *
app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', HomeView.as_view(), name='shop'),
    path('shopsingle/<slug>/', ItemDetailView.as_view(), name= 'shopsingle'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('search/', views.search, name='search'),
    path('cart/', OrderSummaryView.as_view(), name='cart'),
path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('checkout/', views.checkOut, name='checkout'),
    path('registration/', views.Pharegister, name='registration'),
    path('contact/', views.contact, name='contact'),
    path('thankyou/', views.thankyou, name='thankyou'),

    path('about', views.about, name='about'),
]
