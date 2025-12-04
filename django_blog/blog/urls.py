from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('search/', views.search_posts, name='search_posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Comment URLs
    path('post/<int:post_pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # Tag filtering
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]
