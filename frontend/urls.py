from django.urls import path, include

from car.views import CarListView, CarDetailView
from booking.views import BookingCreateView
from django.conf.urls.i18n import i18n_patterns




urlpatterns = [
   

        path('', CarListView.as_view(), name='car_list'),
        path('cars/<int:pk>', CarDetailView.as_view(), name='car_detail'),
        path('booking/', BookingCreateView.as_view(), name='create_book')

    
    
] 

