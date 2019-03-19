from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('albums/', views.albums, name='blog-albums'),
    path('artists/', views.artists, name='blog-artists'),
    path('songs/', views.songs, name='blog-songs'),
]
