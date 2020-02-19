
from django.urls import path, include
from booking.rest import BookingViewSet
from car.rest import CarViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('booking', BookingViewSet)
router.register('cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls))
] 