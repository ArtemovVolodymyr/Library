# author/admin.py

from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')  

admin.site.register(Author, AuthorAdmin)