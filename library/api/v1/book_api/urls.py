from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path('api/v1/book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
