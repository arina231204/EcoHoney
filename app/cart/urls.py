from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('get_total_sum/', views.cart_total_sum, name='get_total_sum'),
    path('get_count/', views.cart_count, name='get_count'),
    path('clear/', views.cart_clear, name='clear'),
]


