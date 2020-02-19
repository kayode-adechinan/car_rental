# Create your views here.
from rest_framework import viewsets
from booking import models, serializers


# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
