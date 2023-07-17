from django.urls import path
from . import views

urlpatterns = [
    path('librarian/authors/', views.index_author, name='index_author'),
    path('librarian/authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('librarian/authors/create/', views.create_author, name='author-create'),
    path('librarian/authors/delete/<int:author_id>/', views.delete_author, name='delete_author'),
    path('librarian/authors/update/<int:author_id>/', views.update_author, name='update_author'),

]

