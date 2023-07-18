from rest_framework import serializers
from author.models import Author
#from django.contrib.auth.models import User
from authentication.models import CustomUser
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many = True, queryset=CustomUser.objects.all())
    class Meta:
        model = CustomUser
        fields = ["id", "email"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'patronymic', 'books')