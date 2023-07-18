from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from author.models import Author
from .serializers import AuthorSerializer


class AuthorView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    