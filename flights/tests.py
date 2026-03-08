from django.test import TestCase
from .models import Flight

class FlightModelTest(TestCase):
    def setUp(self):
        # Create a "dummy" flight for testing
        self.flight = Flight.objects.create(
            flight_number="CH777",
            destination="London",
            departure_time="2026-05-01 12:00:00+00:00",
            price=150.00
        )

    def test_flight_creation(self):
        """Test that the flight was created with the correct data"""
        self.assertEqual(self.flight.destination, "London")
        self.assertEqual(str(self.flight), "CH777 to London")
