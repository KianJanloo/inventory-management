from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product-list'),
    path('create/', views.product_create_view, name='product-create'),
    path('update/<int:product_id>/', views.product_update_view, name='product-update'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product-delete'),
]