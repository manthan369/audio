from django.contrib import admin

# Register your models here.
from .models import Song, Podcast, Audiobook, AudioFileType

admin.site.register(Song)
admin.site.register(Podcast)
admin.site.register(Audiobook)
admin.site.register(AudioFileType)