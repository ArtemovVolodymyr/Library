from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import BasePermission

from author.models import Author
from .serializers import AuthorSerializer

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1

class AuthorView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsLibrarian]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    