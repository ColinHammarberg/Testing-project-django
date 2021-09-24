from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/<order_number>', views.success, name='success'),

]