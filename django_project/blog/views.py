from django.shortcuts import render
from .models import Song, Artist, Album, Songartist, Songalbum, Albumartist

def home(request):
	songs = Song.objects.all()
	artists = Artist.objects.all()
	albums = Album.objects.all()

	songids = Song.objects.values('id')

	songartistdict = dict()
	for i in Songartist.objects.filter(song_id__in=songids).values('artist_id', 'song_id'):
		if i['song_id'] in songartistdict:
			# append the new number to the existing array at this slot
			songartistdict[i['song_id']].append(i['artist_id'])
		else:
			# create a new array in this slot
			songartistdict[i['song_id']] = [i['artist_id']]

	songalbumdict = dict()
	for i in Songalbum.objects.filter(song_id__in=songids).values('album_id', 'song_id'):
		songalbumdict[i['song_id']] = i['album_id']

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
	album = Album.objects.filter(id=albumid).first()

	song_ids = Song.objects.values('id')

	song_id_list=list()
	for i in Songalbum.objects.filter(song_id__in=song_ids, album_id=albumid).values('song_id'):
		song_id_list.append(i['song_id'])

	songs = Song.objects.filter(id__in=song_id_list)

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
	artist = Artist.objects.filter(id=artistid).first()

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

	songids = Song.objects.values('id')
	songartistdict = dict()
	for i in Songartist.objects.filter(song_id__in=songids).values('artist_id', 'song_id'):
		if i['song_id'] in songartistdict:
			# append the new number to the existing array at this slot
			songartistdict[i['song_id']].append(i['artist_id'])
		else:
			# create a new array in this slot
			songartistdict[i['song_id']] = [i['artist_id']]

	songalbumdict = dict()
	for i in Songalbum.objects.filter(song_id__in=songids).values('album_id', 'song_id'):
		songalbumdict[i['song_id']] = i['album_id']

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
	song = Song.objects.filter(id=songid).first()

	context = {
		'title': 'song',
		'song': song
	}

	return render(request, 'blog/song.html', context)
