from rest_framework import viewsets
from .models import StationData
from .serializers import StationDataSerializer

class StationDataViewSet(viewsets.ModelViewSet):
    queryset = StationData.objects.all()
    serializer_class = StationDataSerializer
