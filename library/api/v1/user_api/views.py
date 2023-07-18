from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from authentication.models import CustomUser
from order.models import Order
from .serializers import UserSerializer, OrderSerializer
from book.models import Book

@api_view(['POST', 'GET'])
def signup_or_login(request):
    if request.method == "POST":
        if request.data["action"] == "register": 
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                user = CustomUser.objects.get(email = request.data['email'])
                user.set_password(request.data["password"])
                user.save()
                
                token = Token.objects.create(user=user)
                return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.data["action"] == "login":
            user = get_object_or_404(CustomUser, email = request.data["email"])
        
            if not user.check_password(request.data['password']):
                return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(instance=user)
            
            return Response({"token":token.key, "user": serializer.data}, status=status.HTTP_200_OK)
    else:
        if request.user.role != 1:
            return Response("Acces restricted!", status=status.HTTP_403_FORBIDDEN)
        users = CustomUser.objects.all()
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PATCH', "DELETE"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request, user_id):
    if request.user.id != user_id and request.user.role != 1:
        return Response("Acces restricted!", status=status.HTTP_403_FORBIDDEN)
    user = CustomUser.objects.get(id=user_id)
    
    if request.method == "GET": 
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        first_name = request.data.get("first_name", None)
        middle_name = request.data.get("middle_name", None)
        last_name = request.data.get("last_name", None)
        password = request.data.get("password", None)
        role = request.data.get("role", None)
        
        user.update(first_name=first_name, middle_name=middle_name, last_name=last_name, password=password, role=role)
        serializer = UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        user.delete()
        return Response(f"Deleted user with id {user_id}", status=status.HTTP_200_OK)
    
    
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_order(request, user_id, order_id):
    if request.user.id != user_id and request.user.role != 1:
        return Response("Acces restricted!", status=status.HTTP_403_FORBIDDEN)
    
    order = Order.objects.get(id=order_id)
    
    if request.method == 'POST':
        order.delete()
        return Response(f"Deleted order with id {order_id}", status=status.HTTP_200_OK)
    else:
        serializer = OrderSerializer(instance=order)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def all_user_orders(request, user_id):
    if request.user.id != user_id and request.user.role != 1:
        return Response("Acces restricted!", status=status.HTTP_403_FORBIDDEN)
    if request.method == "GET":
        orders = Order.objects.filter(user_id=user_id)
        
        serializer = OrderSerializer(instance=orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        book = Book.objects.get(id = int(request.data.get('book'))) 
        user = CustomUser.objects.get(id = user_id)
        plated_end_at = request.data.get('plated_end_at')
        
        new_order = Order.objects.create(user=user, book=book, plated_end_at=plated_end_at)
        
        serializer = OrderSerializer(instance=new_order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
