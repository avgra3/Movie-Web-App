from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, 
                    PostUpdateView, PostDeleteView, UserPostListView, 
                    MoviesListView, DirectorsListView, MoviesDetailView,
                    DirectorsDetailView)

# Url paths for all movie app
urlpatterns = [
    path('', views.home, name='movie-home'),
    path('movies/', MoviesListView.as_view(), name='movie-movies'),
    path('movies/<int:pk>/', MoviesDetailView.as_view(), name='movie-movies-detail'),
    
    path('directors/', DirectorsListView.as_view(), name='movie-directors'),
    path('directors/<int:pk>/', DirectorsDetailView.as_view(), name='movie-directors-detail'),
    
    path('reviews/', PostListView.as_view(), name='movie-reviews'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('reviews/post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
