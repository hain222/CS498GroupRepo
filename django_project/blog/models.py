# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    image = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=15)
    rel_date = models.CharField(max_length=32, blank=True, null=True)
    num_tracks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Album'


class Albumartist(models.Model):
    album = models.ForeignKey(Album, models.DO_NOTHING, primary_key=True)
    artist = models.ForeignKey('Artist', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AlbumArtist'
        unique_together = (('album', 'artist'),)


class Artist(models.Model):
    id = models.CharField(primary_key=True, max_length=22)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'Artist'


class Song(models.Model):
    duration = models.IntegerField()
    id = models.CharField(primary_key=True, max_length=22)
    link = models.CharField(max_length=100)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'Song'


class Songalbum(models.Model):
    album = models.ForeignKey(Album, models.DO_NOTHING, primary_key=True)
    song = models.ForeignKey(Song, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'SongAlbum'
        unique_together = (('album', 'song'),)


class Songartist(models.Model):
    song = models.ForeignKey(Song, models.DO_NOTHING)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'SongArtist'
        unique_together = (('artist', 'song'),)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'User'
