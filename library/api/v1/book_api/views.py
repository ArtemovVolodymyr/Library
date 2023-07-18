from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from book.models import Book
from .serializers import BookSerializer


class BookDetailView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
