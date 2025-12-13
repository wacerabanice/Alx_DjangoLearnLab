from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet


router = DefaultRouter()
path('feed/', FeedView.as_view(), name='feed'),
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [
path('', include(router.urls)),
]