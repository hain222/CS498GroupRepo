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
	userId INT PRIMARY KEY,
	username VARCHAR(32) NOT NULL,
	password VARCHAR(32) NOT NULL
);

CREATE TABLE Song (
	songId VARCHAR(22) NOT NULL PRIMARY KEY,
	name VARCHAR(64) NOT NULL
);

CREATE TABLE Artist (
	artistId VARCHAR(22) NOT NULL PRIMARY KEY,
	name VARCHAR(64) NOT NULL
);

CREATE TABLE Album (
	albumId VARCHAR(22) NOT NULL PRIMARY KEY,
	albumImg VARCHAR(128),
	albumName VARCHAR(64) NOT NULL,
	albumType VARCHAR(15) NOT NULL, -- types include: single, album, or compilation
	relDate VARCHAR(32),
	numTracks INT
);

CREATE TABLE SongAlbum (
	albumId VARCHAR(22) NOT NULL,
	songId VARCHAR(22) NOT NULL,
	PRIMARY KEY (songId, albumId),
	FOREIGN KEY(songId) REFERENCES Song(songId),
	FOREIGN KEY(albumId) REFERENCES Album(albumId)
);

CREATE TABLE SongArtist (
	artistId VARCHAR(22) NOT NULL,
	songId VARCHAR(22) NOT NULL,
	PRIMARY KEY (songId, artistId),
	FOREIGN KEY(songId) REFERENCES Song(songId),
	FOREIGN KEY(artistId) REFERENCES Artist(artistId)
);

CREATE TABLE AlbumArtist (
	albumId VARCHAR(22) NOT NULL,
	artistId VARCHAR(22) NOT NULL,
	PRIMARY KEY (albumId, artistId),
	FOREIGN KEY(albumId) REFERENCES Album(albumId),
	FOREIGN KEY(artistId) REFERENCES Artist(artistId)
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
