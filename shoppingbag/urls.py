from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingbag, name='shoppingbag'),
    path('add/<item_id>/', views.add_product, name='add_product'),
]
