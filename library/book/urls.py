# book/urls.py

from django.urls import path
from .import views

urlpatterns = [
    path('books/', views.index_book, name='index_book'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('book/create/', views.create_book, name='create_book'),    
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('books/update/<int:book_id>/', views.update_book, name='update_book'),
]
