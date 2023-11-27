
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostCreateView, BlogPostDetailView, BlogPostUpdateView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog_list'),
    path('create/', BlogPostCreateView.as_view(), name='blog_create'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('update/<int:pk>/', BlogPostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blog_confirm_delete'),
]
