from booking.models import Booking
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


class BookingCreateView(SuccessMessageMixin, CreateView):
    model = Booking
    fields = (
        "car",
        "customer_name",
        "customer_email",
        "customer_phone_number",
        "booking_start_date",
        "booking_end_date",
    )
    template_name = "car/detail.html"
    success_url = reverse_lazy("car_list")
    success_message = "You have successfully created a booking for this car. \
                                    Someone from our staff will contact you shortly."
