from .models import AudioFileType
from .serializers import AudioFileTypeSerializer
from rest_framework import generics

class AudioCreate(generics.CreateAPIView):
    queryset = AudioFileType.objects.all()
    serializer_class = AudioFileTypeSerializer

class AudioDelete(generics.DestroyAPIView):
    queryset = AudioFileType.objects.all()
    serializer_class = AudioFileTypeSerializer

class AudioUpdate(generics.UpdateAPIView):
    queryset = AudioFileType.objects.all()
    serializer_class = AudioFileTypeSerializer

class AudioList(generics.ListAPIView):
    queryset = AudioFileType.objects.all()
    serializer_class = AudioFileTypeSerializer