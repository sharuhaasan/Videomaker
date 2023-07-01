from rest_framework import serializers
from .models import AudioElement

class AudioElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioElement
        fields = ['id', 'type', 'high_volume', 'low_volume', 'video_component_id', 'url', 'duration_start_time', 'duration_end_time']
