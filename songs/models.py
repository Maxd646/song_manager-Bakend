from django.db import models

from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True, null=True)
    year = models.PositiveIntegerField()
    audio_file = models.FileField(upload_to='audios/', blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"
