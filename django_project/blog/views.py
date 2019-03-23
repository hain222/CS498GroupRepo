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


	return render(
		request,
		'blog/albums.html',
		{
			'title': 'Albums',
			'albums': albums,
		}
	)

def album(request, albumid):
	album = Album.objects.filter(albumid=albumid).first()

	songids = Song.objects.values('songid')

	songidlist=list()
	for i in Songalbum.objects.filter(songid__in=songids,albumid=albumid).values('songid'):
		songidlist.append(i['songid'])

	songs = Song.objects.filter(songid__in=songidlist)

	return render(
		request,
		'blog/album.html',
		{
			'title': 'album',
			'album': album,
			'songs': songs
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

def artist(request, artistid):
	artist = Artist.objects.filter(artistid=artistid).first()

	return render(
		request,
		'blog/artist.html',
		{
			'title': 'Artists',
			'artist': artist
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

def song(request, songid):
	song = Song.objects.filter(songid=songid).first()

	context = {
		'title': 'song',
		'song': song
	}

	return render(request, 'blog/song.html', context)
