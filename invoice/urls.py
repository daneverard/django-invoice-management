from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_invoice, name='home'),
    
    path('create_product/', views.create_product, name='create_product'),
    path('view_product/', views.view_product, name='view_product'),
    path('edit_product/<int:pk>', views.edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),

    path('create_customer/', views.create_customer, name='create_customer'),
    path('view_customer/', views.view_customer, name='view_customer'),
    path('edit_customer/<int:pk>', views.edit_customer, name='edit_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),

    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('view_invoice/', views.view_invoice, name='view_invoice'),
    path('delete_invoice/<int:pk>/', views.delete_invoice, name='delete_invoice'),

    path('view_invoice_detail/<int:pk>/', views.view_invoice_detail, name='view_invoice_detail'),
]
