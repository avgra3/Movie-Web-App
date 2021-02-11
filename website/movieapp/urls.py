from django.urls import path
from . import views

# Url paths for all movie app
urlpatterns = [
    path('', views.home, name='movie-home'),
    path('movies/', views.movies, name='movie-movies'),
    path('directors/', views.directors, name='movie-directors'),
]
