from django.shortcuts import render
from .models import Song, Songartist, Artist, Album, Songalbum


def home(request):
	songs = Song.objects.all()
	artists = Artist.objects.all()
	albums = Album.objects.all()

	songids = Song.objects.values('songid')
	# artistids = Songartist.objects.filter(songid__in=songids).values('artistid')
	# artists = Artist.objects.filter(artistid__in=artistids)

	songartistdict = dict()
	for i in Songartist.objects.filter(songid__in=songids).values('artistid', 'songid'):
		if i['songid'] in songartistdict:
			# append the new number to the existing array at this slot
			songartistdict[i['songid']].append(i['artistid'])
		else:
			# create a new array in this slot
			songartistdict[i['songid']] = [i['artistid']]

	songalbumdict = dict()
	for i in Songalbum.objects.filter(songid__in=songids).values('albumid', 'songid'):
		# print(i)
		songalbumdict[i['songid']] = i['albumid']


	context = {
		'songs': songs,
		'artists': artists,
		'albums': albums,
		'songartistdict': songartistdict,
		'songalbumdict': songalbumdict
	}

	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
