#!/usr/bin/env python3

# autotesting script
# contains tests for database sanity checking

# T1 tests the song to album relations
# T2 tests the song to artist relations
# T3 tests the album to artist relations

import pymysql as sql

db = sql.connect("localhost","root","DogMonkeyTable","isdb")
cursor = db.cursor()
testArray = []

t1 = ("High Hopes","Pray For The Wicked")
t2 = ("High Hopes","Panic! At The Disco")
t3 = ("Pray For The Wicked","Panic! At The Disco")

# TEST 1
query = "SELECT Song.name,Album.name FROM Song,SongAlbum,Album WHERE Song.songId = SongAlbum.songId AND Album.albumId = SongAlbum.albumId AND Song.name = 'High Hopes'"
cursor.execute(query)
if cursor.rowcount == 1:
	data = cursor.fetchone()
	if data == t1:
		testArray.append("SUCCESS")
	else:
		testArray.append("FAIL")
else:
	testArray.append("FAIL")

# TEST 2
query = "SELECT Song.name,Artist.name FROM Song,SongArtist,Artist WHERE Song.songId = SongArtist.songId AND Artist.artistId = SongArtist.artistId AND Song.name = 'High Hopes'"
cursor.execute(query)
if cursor.rowcount == 1:
	data = cursor.fetchone()
	if data == t2:
		testArray.append("SUCCESS")
	else:
		testArray.append("FAIL")
else:
	testArray.append("FAIL")

# TEST 3
query = "SELECT Album.name,Artist.name FROM Album,AlbumArtist,Artist WHERE Album.albumId = AlbumArtist.albumId AND Artist.artistId = AlbumArtist.artistId AND Album.name = 'Pray For The Wicked'"
cursor.execute(query)
data = cursor.fetchone()
if data == t3:
	testArray.append("SUCCESS")
else:
	testArray.append("FAIL")

print(testArray)

db.close()
