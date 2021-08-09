"""Post models admin."""

# Django
from django.contrib import admin

# Models
from blog.posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post model admin."""
    list_display = ('user', 'title')
    search_fields = ('title', 'user__username')
