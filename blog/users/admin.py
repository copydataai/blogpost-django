"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from blog.users.models import User, Profile

class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'first_name', 'last_name', 'is_client')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""
    list_display = ('user', 'picture')


admin.site.register(User, CustomUserAdmin)
