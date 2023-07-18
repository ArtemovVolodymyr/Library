from django.shortcuts import render
from rest_framework import viewsets, generics

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import BasePermission

from order.models import Order
from .serializers import OrderSerializer

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 1

class OrderView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsLibrarian]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    