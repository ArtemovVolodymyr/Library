from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from authentication.models import CustomUser
from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(email = request.data['email'])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(CustomUser, email = request.data["email"])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token":token.key, "user": serializer.data}, status=status.HTTP_200_OK)

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