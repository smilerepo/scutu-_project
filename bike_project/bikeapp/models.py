# bikeapp/models.py

from django.db import models


class Bike(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100) #model of the bikescooter entry
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Rider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class BikeAllotment(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    date_allotted = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.bike.name} allotted to {self.rider.name}'

class Payment(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rider.name} - {self.amount}'
