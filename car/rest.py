# Create your views here.
from rest_framework import viewsets
from car import models, serializers, filters


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    filterset_class = filters.CarFilter
