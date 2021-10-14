from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoppingbag, name='shoppingbag'),
    path('add/<item_id>/', views.add_product, name='add_product'),
    path('remove/<item_id>/', views.remove_product, name='remove_product'),
]
