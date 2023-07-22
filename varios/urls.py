from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página de inicio de la tienda, muestra una lista de productos
    path('', views.product_list, name='product_list'),

    # Ruta para ver los detalles de un producto en particular
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
