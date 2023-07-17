from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
from .forms import UserCreationForm, UserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('__str__', 'is_staff', 'is_superuser',)
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'is_active', 'password',)}),
        ('Personal information', {'fields': ('first_name', 'last_name', 'middle_name', 'role',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2',)}),
        ('Personal information', {'fields': ('first_name', 'last_name', 'middle_name', 'role',)}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
