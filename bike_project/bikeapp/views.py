# bikeapp/views.py

from rest_framework import viewsets
from .models import Bike, Rider, BikeAllotment, Payment
from .serializers import BikeSerializer, RiderSerializer, BikeAllotmentSerializer, PaymentSerializer

class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

class BikeAllotmentViewSet(viewsets.ModelViewSet):
    queryset = BikeAllotment.objects.all()
    serializer_class = BikeAllotmentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# bikeapp/views.py

from django.shortcuts import render
from .models import Bike, Rider, BikeAllotment, Payment



def index(request):
    return render(request, 'bikeapp/index.html')

def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'bikeapp/bikes.html', {'bikes': bikes})

# Similarly, you can create views for riders, bike allotments, and payments
