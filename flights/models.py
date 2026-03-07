from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} to {self.destination}"

class Booking(models.Model):
    # This links the booking to a specific User and Flight
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_preference = models.CharField(max_length=10, choices=[('Window', 'Window'), ('Aisle', 'Aisle')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number}"
