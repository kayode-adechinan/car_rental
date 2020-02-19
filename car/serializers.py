from rest_framework import serializers
from car.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "image",
            "description",
            "daily_rent",
            "type",
            "category",
            "brand",
            "model",
            "is_available",
        )
        model = Car
