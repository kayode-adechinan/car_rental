from rest_framework import serializers
from booking.models import Booking



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "car",
            "customer_name",
            "customer_email",
            "customer_phone_number",
            "booking_start_date",
            "booking_end_date",
        )
        model = Booking
