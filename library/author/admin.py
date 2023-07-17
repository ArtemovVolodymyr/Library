from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'surname',)
    list_display = ('name', 'surname',)
