from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
# This is the "Model" part of the MVC (Model-View-Controller) pattern.
class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True) # e.g., LHR, JFK
    name = models.CharField(max_length=100)           # e.g., Heathrow
    city = models.CharField(max_length=100)           # e.g., London

    def __str__(self):
        return f"{self.city} ({self.code})"
     
# This is the "Flight" model, which represents a flight in our system.       
class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    # These link to the Airport model above
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight_image = CloudinaryField('image', default='placeholder')
    capacity = models.PositiveIntegerField(default=150) # Total seats on the plane
    
    # This is a "property" - it calculates seats remaining on the fly
    @property
    def seats_remaining(self):
        # Count only 'Confirmed' bookings
        confirmed_bookings = self.booking_set.filter(status='Confirmed').count()
        return self.capacity - confirmed_bookings
        
    def __str__(self):
        return f"{self.flight_number}: {self.origin} to {self.destination}"

class Booking(models.Model):
    # This links the booking to a specific User and Flight
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    seat_preference = models.CharField(max_length=10, choices=[('Window', 'Window'), ('Aisle', 'Aisle')])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.flight.flight_number} ({self.status})"
    
class PassengerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    passport_number = models.CharField(max_length=20, blank=True)
    frequent_flyer_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
