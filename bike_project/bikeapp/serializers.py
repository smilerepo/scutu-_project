# bikeapp/serializers.py

from rest_framework import serializers
from .models import Bike, Rider, BikeAllotment, Payment

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'

class BikeAllotmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeAllotment
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
