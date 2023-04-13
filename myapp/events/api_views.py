from rest_framework import generics
from ..models import Event
from .serializers import EventSerializer
from .permissions import IsOrganizer
from .permissions import IsAuthenticatedOrOrganizer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [IsAuthenticatedOrOrganizer]

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [IsAuthenticatedOrOrganizer]