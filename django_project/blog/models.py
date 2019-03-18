# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Album(models.Model):
    albumid = models.CharField(db_column='albumId', primary_key=True, max_length=22)  # Field name made lowercase.
    albumimg = models.CharField(db_column='albumImg', max_length=128, blank=True, null=True)  # Field name made lowercase.
    albumname = models.CharField(db_column='albumName', max_length=64)  # Field name made lowercase.
    albumtype = models.CharField(db_column='albumType', max_length=15)  # Field name made lowercase.
    reldate = models.CharField(db_column='relDate', max_length=32, blank=True, null=True)  # Field name made lowercase.
    numtracks = models.IntegerField(db_column='numTracks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Album'


class Albumartist(models.Model):
    albumid = models.ForeignKey(Album, models.DO_NOTHING, db_column='albumId', primary_key=True)  # Field name made lowercase.
    artistid = models.ForeignKey('Artist', models.DO_NOTHING, db_column='artistId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlbumArtist'
        unique_together = (('albumid', 'artistid'),)


class Artist(models.Model):
    artistid = models.CharField(db_column='artistId', primary_key=True, max_length=22)  # Field name made lowercase.
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'Artist'


class Song(models.Model):
    songid = models.CharField(db_column='songId', primary_key=True, max_length=22)  # Field name made lowercase.
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'Song'


class Songalbum(models.Model):
    albumid = models.ForeignKey(Album, models.DO_NOTHING, db_column='albumId')  # Field name made lowercase.
    songid = models.ForeignKey(Song, models.DO_NOTHING, db_column='songId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SongAlbum'
        unique_together = (('songid', 'albumid'),)


class Songartist(models.Model):
    artistid = models.ForeignKey(Artist, models.DO_NOTHING, db_column='artistId')  # Field name made lowercase.
    songid = models.ForeignKey(Song, models.DO_NOTHING, db_column='songId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SongArtist'
        unique_together = (('songid', 'artistid'),)


class User(models.Model):
    userid = models.IntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
