from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('netflix/', views.netflix, name='netflix'),
    path('spotify-login/', views.spotifyLogin, name='spotify'),
    path('spotify/', views.spotify, name='spotify'),
    path('youtube/', views.youtube, name='youtube'),
    path('snake/', views.snake, name='snake'),
]
