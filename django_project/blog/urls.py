from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),

    path('about/', views.about, name='blog-about'),

    path('albums/', views.albums, name='blog-albums'),
    path('albums/<albumid>', views.album, name='blog-album'),

    path('artists/', views.artists, name='blog-artists'),
    path('artists/<artistid>', views.artist, name='blog-artist'),

    path('songs/', views.songs, name='blog-songs'),
    path('songs/<songid>', views.song, name='blog-song'),
]
