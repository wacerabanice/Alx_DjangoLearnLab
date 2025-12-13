from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from .views import NotificationListView
from .views import LikePostView, UnlikePostView


router = DefaultRouter()
path('feed/', FeedView.as_view(), name='feed'),
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
path('', NotificationListView.as_view(), name='notifications'),

urlpatterns = [
path('', include(router.urls)),
]