from django.shortcuts import render
from car.models import Car
from car.filters import CarFilter
from booking.models import Booking
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin



class IndexView1(ListView):
    model = Car
    template_name = "frontend/index.html"
    context_object_name = 'cars'  # Default: object_list
    paginate_by = 1
    #queryset = Car.objects.all()  # Default: Model.objects.all()

    def get_queryset(self):
        qs = self.model.objects.all()
        product_filtered_list = CarFilter(self.request.GET, queryset=qs)
        return product_filtered_list.qs
    

class IndexView(FilterView):
    template_name = "frontend/index.html"
    context_object_name = 'cars'  # Default: object_list
    paginate_by = 10
    filterset_class= CarFilter


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['message'] = "back to django"
        return context



class CarDetailView(DetailView):
    model = Car
    template_name = 'frontend/detail.html'
    context_object_name = 'car'



class BookingCreateView(SuccessMessageMixin, CreateView):
    model = Booking
    fields = (
        'car',
        'customer_name',
        'customer_email',
        'customer_phone_number',
        'booking_start_date',
        'booking_end_date',
    
    
    )
    template_name = 'frontend/detail.html'
    success_url = reverse_lazy('index')
    success_message = "You have successfully created a booking for this car. Someone from our staff will contact you shortly."
