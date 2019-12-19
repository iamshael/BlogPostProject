from django.urls import path
from .views import (PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blogapp-home'), #Custom convention see views.py
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#default convention
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),#default convention
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),#default convention
    path('post/new/', PostCreateView.as_view(), name='post-create'), #default convention
    path('about/', views.about, name='blogapp-about'),
]
