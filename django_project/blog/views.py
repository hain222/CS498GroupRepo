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

def login(request):
	return render(
		request,
		'registration/login.html',
		{
			'title': 'Login'
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
	song_id_list = list()
	for i in Songalbum.objects.filter(song_id__in=song_ids, album_id=albumid).values('song_id'):
		song_id_list.append(i['song_id'])
	songs = Song.objects.filter(id__in=song_id_list)

	artist_ids = Artist.objects.values('id')
	artist_id_list = list()
	for i in Albumartist.objects.filter(artist_id__in=artist_ids, album_id=albumid).values('artist_id'):
		artist_id_list.append(i['artist_id'])
	artists = Artist.objects.filter(id__in=artist_id_list)

	return render(
		request,
		'blog/album.html',
		{
			'title': album.name,
			'album': album,
			'songs': songs,
			'artists': artists
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

	songs = Song.objects.all()
	songids = Song.objects.values('id')
	artist_song_ids = list()
	for i in Songartist.objects.filter(song_id__in=songids).values('artist_id', 'song_id'):
		if i['artist_id'] == artistid:
			artist_song_ids.append(i)

	albums = Album.objects.all()
	albumids = Album.objects.values('id')
	artist_album_ids = list()
	for i in Albumartist.objects.filter(album_id__in=albumids).values('artist_id', 'album_id'):
		if i['artist_id'] == artistid:
			artist_album_ids.append(i)

	return render(
		request,
		'blog/artist.html',
		{
			'title': artist.name,
			'artist': artist,
			'artist_song_ids': artist_song_ids,
			'songs': songs,
			'artist_album_ids': artist_album_ids,
			'albums': albums
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

	artist_ids = Artist.objects.values('id')
	artist_id_list = list()
	for i in Songartist.objects.filter(artist_id__in=artist_ids, song_id=songid).values('artist_id'):
		artist_id_list.append(i['artist_id'])
	artists = Artist.objects.filter(id__in=artist_id_list)

	albums_ids = Album.objects.values('id')
	album_id_list = list()
	for i in Songalbum.objects.filter(album_id__in=albums_ids, song_id=songid).values('album_id'):
		album_id_list.append(i['album_id'])
	album = Album.objects.filter(id__in=album_id_list).first()

	duration = song.duration
	# print(duration)
	s = duration / 1000
	m,s = divmod(s, 60)
	h,m = divmod(m, 60)
	d,h = divmod(h, 24)
	s = '0' + str(int(s)) if int(s) < 10 else str(int(s))
	m = '0' + str(int(m)) if int(m) < 10 else str(int(m))
	h = '0' + str(int(h)) if int(h) < 10 else str(int(h))
	d = '0' + str(int(d)) if int(d) < 10 else str(int(d))
	time = '{}:{}:{}:{}'.format(d, h, m, s)
	if d == '00' and h == '00':
		time = time[6:]
	elif d == '00':
		time = time[3:]

	context = {
		'title': song.name,
		'song': song,
		'time': time,
		'artists': artists,
		'album': album
	}

	return render(request, 'blog/song.html', context)
