import django_filters
from car import models


class CarFilter(django_filters.FilterSet):
    class Meta:
        fields = {
            "name": ["exact", "icontains"],
            "daily_rent":["range", "lte", "gte"],
            "type":["exact"],
            "category":["exact"],
            "brand":["exact"],
            "model":["exact"],
            "is_available":["exact"],
        }
        model = models.Car
