from django.shortcuts import render
from .models import Song


def home(request):
	songs = Song.objects.all()

	context = {
		'songs': songs

	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
