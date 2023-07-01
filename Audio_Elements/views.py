from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AudioElement
from .serializers import AudioElementSerializer

class AudioElementListCreateView(generics.ListCreateAPIView):
    queryset = AudioElement.objects.all()
    serializer_class = AudioElementSerializer

    def post(self, request, *args, **kwargs):
        video_component_id = request.data.get('video_component_id')
        if video_component_id:
            # Check if there are overlapping audio elements of the same type
            overlapping_elements = AudioElement.objects.filter(video_component_id=video_component_id,
                                                               type=request.data['type'],
                                                               duration_end_time__gt=request.data[
                                                                   'duration_start_time'],
                                                               duration_start_time__lt=request.data[
                                                                   'duration_end_time'])
            if overlapping_elements.exists():
                # Adjust the start time and end time of the new audio element
                last_end_time = overlapping_elements.order_by('-duration_end_time').first().duration_end_time
                request.data['duration_start_time'] = last_end_time
                request.data['duration_end_time'] = last_end_time + (
                            request.data['duration_end_time'] - request.data['duration_start_time'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class AudioElementRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AudioElement.objects.all()
    serializer_class = AudioElementSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            if instance.type == 'video_audio':
                # Populate duration and url from the corresponding video-block
                video_component = instance.video_component
                serializer.data['duration'] = video_component.duration
                serializer.data['url'] = video_component.url

            return Response(serializer.data, status=status.HTTP_200_OK)
        except AudioElement.DoesNotExist:
            return Response({'detail': 'Audio element not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        audio_element = self.get_object()
        if audio_element.type == 'video_music':
            # Do not delete the original video component
            audio_element.video_component_id = None
            audio_element.url = None
            audio_element.save()
        self.perform_destroy(audio_element)
        return Response(status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # If the audio element is of type "video_music", ignore updating the video component
        if instance.type == 'video_music' and 'video_component_id' in request.data:
            del request.data['video_component_id']

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AudioFragmentListView(APIView):
    def get(self, request, start_time, end_time):
        audio_elements = AudioElement.objects.filter(duration_end_time__gt=start_time, duration_start_time__lt=end_time)
        audio_fragments = []

        for audio_element in audio_elements:
            # Calculate the volume of the audio fragment
            volume = 'High Volume' if audio_element.high_volume else 'Low Volume'

            # Adjust the start time and end time if they fall outside the range
            fragment_start_time = max(audio_element.duration_start_time, start_time)
            fragment_end_time = min(audio_element.duration_end_time, end_time)

            # Create the audio fragment dictionary
            fragment = {
                'type': audio_element.type,
                'start_time': fragment_start_time,
                'end_time': fragment_end_time,
                'volume': volume
            }

            audio_fragments.append(fragment)

        return Response(audio_fragments, status=status.HTTP_200_OK)