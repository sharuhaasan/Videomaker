from django.db import models
import uuid


class AudioElement(models.Model):
    AUDIO_TYPES = (
        ('vo', 'Voice Over'),
        ('bg_music', 'Background Music'),
        ('video_music', 'Video Music'),
    )

    id = models.IntegerField(primary_key=True)
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=AUDIO_TYPES)
    high_volume = models.FloatField()
    low_volume = models.FloatField()
    video_component_id = models.UUIDField(null=True)  # assuming video_component_id is UUIDField
    #video_component_id = models.ForeignKey('video_elements.VideoComponent', on_delete=models.CASCADE, null=True)
    url = models.URLField(null=True)
    duration_start_time = models.FloatField(null=True)  # Null if type is video_music
    duration_end_time = models.FloatField(null=True)  # Null if type is video_music

    def __str__(self):
        return f"{self.type} - {self.url}"

