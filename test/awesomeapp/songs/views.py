from django.shortcuts import render
from .models import Song

# Create your views here.


def home(request):
    songs = Song.objects.all()

    return render(
        request,
        'songs/home.html',
        {
            'songs': songs
        }
    )
