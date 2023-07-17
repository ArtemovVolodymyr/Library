from .models import Book
from django.contrib import admin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'author', 'description')
    list_display = ('id', 'name', 'description', 'count')
    list_filter = ('name', 'id', 'description', 'count')
    sortable_by = ('id', 'name', 'author', 'description')
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('name','description','count')}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name', 'author', )
        return self.readonly_fields


