"""Posts URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import posts as posts_views

router = DefaultRouter()
router.register(r'posts', posts_views.PostViewSet, basename='posts')


urlpatterns = [
    path('', include(router.urls))
]
