from django.urls import path
from . import views

urlpatterns = [
    path('librarian/orders/', views.librarian_orders_view, name='librarian-orders'),
    path('visitor/orders/', views.visitor_orders_view, name='visitor-orders'),
    path('librarian/orders/<int:order_id>/close/', views.order_close, name='order-close'),
    path('librarian/orders/create/', views.order_create_view, name='order-create'),
    path('librarian/orders/<int:order_id>/', views.order_view, name='order'),
    
    
]
