from django.shortcuts import render
from .models import Song

# Create your views here.

def home(request):
    songs = Song.objects.all()

    song_ids = Song.objects.values('songid')
    albums = Album.objects.filter('')

    return render(
        request,
        'songs/home.html',
        {
            'songs': songs
        }
    )
