from .models import Song, Podcast, Audiobook, AudioFileType
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = '__all__'

class AudioFileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFileType
        fields = '__all__'
