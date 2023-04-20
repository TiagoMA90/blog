from django.urls import path
from .views import PostListView
from .views import PostDetailView
from . import views

# Mapping for the urls
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]