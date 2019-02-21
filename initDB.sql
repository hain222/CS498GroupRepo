/*
Create ISDB SQL Tables
2-17-19
*/

DROP SCHEMA IF EXISTS isdb;
CREATE DATABASE isdb;
USE isdb;

CREATE TABLE User (
	userId INT PRIMARY KEY,
	username VARCHAR(32) NOT NULL,
	password VARCHAR(32) NOT NULL
);

CREATE TABLE Song (
	songId INT NOT NULL PRIMARY KEY,
	name VARCHAR(64) NOT NULL,
	relDate VARCHAR(32)
);

CREATE TABLE Artist (
	artistId INT NOT NULL PRIMARY KEY,
	name VARCHAR(64) NOT NULL
);

CREATE TABLE Album (
	albumId INT NOT NULL PRIMARY KEY,
	name VARCHAR(64) NOT NULL,
	relDate VARCHAR(32),
	numTracks INT
);

CREATE TABLE SongAlbum (
	songId INT NOT NULL,
	albumId INT NOT NULL,
	PRIMARY KEY (songId, albumId),
	FOREIGN KEY(songId) REFERENCES Song(songId),
	FOREIGN KEY(albumId) REFERENCES Album(albumId)
);

CREATE TABLE SongArtist (
	songId INT NOT NULL,
	artistId INT NOT NULL,
	PRIMARY KEY (songId, artistId),
	FOREIGN KEY(songId) REFERENCES Song(songId),
	FOREIGN KEY(artistId) REFERENCES Artist(artistId)
);

CREATE TABLE AlbumArtist (
	albumId INT NOT NULL,
	artistId INT NOT NULL,
	PRIMARY KEY (albumId, artistId),
	FOREIGN KEY(albumId) REFERENCES Album(albumId),
	FOREIGN KEY(artistId) REFERENCES Artist(artistId)
);
