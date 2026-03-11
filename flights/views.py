from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .models import Flight, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

# This handles the list of flights on the homepage
class FlightList(generic.ListView):
    model = Flight
    template_name = 'flights/index.html'
    context_object_name = 'flights'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # This searches the Flight's Origin and Destination airports for the code or city
            return Flight.objects.filter(
                Q(origin__code__icontains=query) | 
                Q(origin__city__icontains=query) |
                Q(destination__code__icontains=query) |
                Q(destination__city__icontains=query)
            )
        return Flight.objects.all()

# This handles the "Create" part of the Custom Model
@login_required(login_url='/accounts/login/')
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
    
    return render(request, 'flights/book_flight.html', {'form': form, 'flight': flight})

# This handles the "Read" part of the Custom Model
@login_required(login_url='/accounts/login/')
def booking_list(request):
# This filters bookings so users only see THEIR own flights
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'flights/my_bookings.html', {'bookings': bookings})

#cancel booking view, only allows users to cancel their own bookings
@login_required(login_url='/accounts/login/')
def cancel_booking(request, booking_id):
    # This ensures only the owner can cancel their own booking
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking successfully cancelled.')
        return redirect('my_bookings')
    
    # create this template in the next step!
    return render(request, 'flights/cancel_confirm.html', {'booking': booking})

#
@login_required(login_url='/accounts/login/')
def edit_booking(request, booking_id):
    # Security: Ensure only the owner can edit
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        # 'instance=booking' tells Django to UPDATE the existing record
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, f'Booking for {booking.flight.destination} updated!')
            return redirect('my_bookings')
    else:
        # Load the form with the current data
        form = BookingForm(instance=booking)
    
    return render(request, 'flights/edit_booking.html', {'form': form, 'booking': booking})
