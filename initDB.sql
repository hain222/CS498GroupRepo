/*
Create ISDB SQL Tables
2-17-19
*/

-- creating database

DROP SCHEMA IF EXISTS isdb;
CREATE DATABASE isdb;
USE isdb;

-- creating tables

CREATE TABLE User (
	id INT,
	username VARCHAR(32) NOT NULL,
	password VARCHAR(32) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Song (
	duration INT NOT NULL,
	id VARCHAR(22) NOT NULL,
	link VARCHAR(53) NOT NULL,
	name VARCHAR(64) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Artist (
	id VARCHAR(22) NOT NULL,
	image VARCHAR(64),
	link VARCHAR(53) NOT NULL,
	name VARCHAR(64) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Album (
	id VARCHAR(22) NOT NULL,
	image VARCHAR(64),
	link VARCHAR(53) NOT NULL,
	name VARCHAR(64) NOT NULL,
	type VARCHAR(15) NOT NULL, -- types include: single, album, or compilation
	rel_date VARCHAR(32),
	num_tracks INT,
	PRIMARY KEY (id)
);

CREATE TABLE SongAlbum (
	album_id VARCHAR(22) NOT NULL,
	song_id VARCHAR(22) NOT NULL,
	PRIMARY KEY (album_id, song_id),
	FOREIGN KEY(album_id) REFERENCES Album(id) ON DELETE CASCADE,
	FOREIGN KEY(song_id) REFERENCES Song(id) ON DELETE CASCADE
);

CREATE TABLE SongArtist (
	song_id VARCHAR(22) NOT NULL,
	artist_id VARCHAR(22) NOT NULL,
	PRIMARY KEY (artist_id, song_id),
	FOREIGN KEY(artist_id) REFERENCES Artist(id) ON DELETE CASCADE,
	FOREIGN KEY(song_id) REFERENCES Song(id) ON DELETE CASCADE
);

CREATE TABLE AlbumArtist (
	album_id VARCHAR(22) NOT NULL,
	artist_id VARCHAR(22) NOT NULL,
	PRIMARY KEY (album_id, artist_id),
	FOREIGN KEY(album_id) REFERENCES Album(id) ON DELETE CASCADE,
	FOREIGN KEY(artist_id) REFERENCES Artist(id) ON DELETE CASCADE
);

-- loading data

LOAD DATA LOCAL
INFILE "/home/jnge223/CS498GroupRepo/data/dat/songs.dat"
INTO TABLE Song
FIELDS TERMINATED BY '|';

LOAD DATA LOCAL
INFILE "/home/jnge223/CS498GroupRepo/data/dat/albums.dat"
INTO TABLE Album
FIELDS TERMINATED BY '|';

LOAD DATA LOCAL
INFILE "/home/jnge223/CS498GroupRepo/data/dat/artists.dat"
INTO TABLE Artist
FIELDS TERMINATED BY '|';

LOAD DATA LOCAL
INFILE "/home/jnge223/CS498GroupRepo/data/dat/song-album.dat"
INTO TABLE SongAlbum
FIELDS TERMINATED BY '|';

LOAD DATA LOCAL
INFILE "/home/jnge223/CS498GroupRepo/data/dat/song-artist.dat"
INTO TABLE SongArtist
FIELDS TERMINATED BY '|';

LOAD DATA LOCAL
INFILE "/home/jnge223/CS498GroupRepo/data/dat/album-artist.dat"
INTO TABLE AlbumArtist
FIELDS TERMINATED BY '|';
