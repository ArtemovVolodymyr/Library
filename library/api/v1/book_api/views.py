from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from book.models import Book
from .serializers import BookSerializer


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
