from django.db import models
from car.models import Car

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars')

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone_number = models.TextField()

    booking_start_date = models.DateField()
    booking_end_date = models.DateField()

    is_approved = models.BooleanField(default=False)
