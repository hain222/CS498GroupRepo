from django.shortcuts import render
from .models import Song, Artist, Album, Songartist, Songalbum, Albumartist

def home(request):
	songs = Song.objects.all()
	artists = Artist.objects.all()
	albums = Album.objects.all()

	songids = Song.objects.values('songid')

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
	return render(
		request,
		'blog/about.html',
		{
			'title': 'About'
		}
	)

def albums(request):
	albums = Album.objects.all()
	songs = Song.objects.all()

	songids = Song.objects.values('songid')

	songalbumdict = dict()
	for i in Songalbum.objects.filter(songid__in=songids).values('albumid', 'songid'):
		if i['albumid'] in songalbumdict:
			# append the new number to the existing array at this slot
			songalbumdict[i['albumid']].append(i['songid'])
		else:
			# create a new array in this slot
			songalbumdict[i['albumid']] = [i['songid']]

	return render(
		request,
		'blog/albums.html',
		{
			'title': 'Albums',
			'albums': albums,
			'songs': songs,
			'songalbumdict': songalbumdict
		}
	)

def artists(request):
	artists = Artist.objects.all()
	return render(
		request,
		'blog/artists.html',
		{
			'title': 'Artists',
			'artists': artists
		}
	)

def songs(request):
	songs = Song.objects.all()
	artists = Artist.objects.all()
	albums = Album.objects.all()

	songids = Song.objects.values('songid')
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
		songalbumdict[i['songid']] = i['albumid']

	context = {
		'title': 'Songs',
		'songs': songs,
		'artists': artists,
		'albums': albums,
		'songartistdict': songartistdict,
		'songalbumdict': songalbumdict
	}

	return render(request, 'blog/songs.html', context)
