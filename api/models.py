from django.db import models
from audio.consts import *

# Create your models here.

class Song(models.Model):
    class Meta(object):
        db_table = 'song'


    song_name = models.CharField(
        'Song_Name', blank=False, max_length=100, db_index=True
    )
    song_durations = models.IntegerField(
        'Song_Durations', blank=True, null=True,
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )

    def __str__(self):
        return self.song_name

class Podcast(models.Model):
    class Meta(object):
        db_table = 'podcast'


    podcast_name = models.CharField(
        'Podcast_Name', blank=False, max_length=100, db_index=True
    )
    podcast_durations = models.IntegerField(
        'Podcast_Durations', blank=True, null=True,
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
    host = models.CharField(
        'Host', blank=False, max_length=100, db_index=True
    )
    participants = models.CharField(
        'Participants', blank=False, max_length=100, db_index=True
    )

    def __str__(self):
        return self.podcast_name

class Audiobook(models.Model):
    class Meta(object):
        db_table = 'audiobook'


    title = models.CharField(
        'Title', blank=False, max_length=100, db_index=True
    )
    author_title = models.CharField(
        'Author_Title', blank=False, max_length=100, db_index=True
    )
    narrator = models.CharField(
        'Narrator', blank=False, max_length=100, db_index=True
    )
    audiobook_durations = models.IntegerField(
        'Audiobook_Durations', blank=True, null=True,
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )

    def __str__(self):
        return self.title

class AudioFileType(models.Model):
    class Meta(object):
        db_table = 'audio_file_type'

    type = models.CharField(
        'Type', blank=False, max_length=100, db_index=True, choices=audio_file_type
    )
    song = models.ManyToManyField(Song)
    podcast = models.ManyToManyField(Podcast)
    audiobook = models.ManyToManyField(Audiobook)

    def __str__(self):
        return self.type