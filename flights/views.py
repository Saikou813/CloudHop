from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Flight, Booking
from .forms import BookingForm

# This handles the list of flights on the homepage
class FlightList(generic.ListView):
    model = Flight
    template_name = 'index.html'
    context_object_name = 'flights'

# This handles the "Create" part of the Custom Model
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # placeholder user until I set up Login
            booking.user = request.user 
            booking.flight = flight
            booking.save()
            # User Notification
            messages.success(request, f'Successfully booked flight to {flight.destination}!')
            return redirect('home')
    else:
        form = BookingForm()
    
    return render(request, 'book_flight.html', {'form': form, 'flight': flight})