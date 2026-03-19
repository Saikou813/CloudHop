from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .models import Flight, Booking
from .forms import BookingForm, ProfileForm  # Added ProfileForm here
from .forms import FlightSearchForm

class FlightList(generic.ListView):
    model = Flight
    template_name = 'flights/index.html'
    context_object_name = 'flights'

    def get_queryset(self):
        # We now get the IDs from the dropdown selections
        origin_id = self.request.GET.get('origin')
        dest_id = self.request.GET.get('destination')
        queryset = Flight.objects.all()

        # Filter by ID because dropdowns send the ID, not the city name
        if origin_id:
            queryset = queryset.filter(origin_id=origin_id)
        
        if dest_id:
            queryset = queryset.filter(destination_id=dest_id)
            
        return queryset

    # This "slaps" the search form into your page context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We pass the user's GET data so the dropdown stays on the city they picked
        context['form'] = FlightSearchForm(self.request.GET or None)
        return context

# This handles the "Create" part of the Custom Model
@login_required(login_url='/accounts/login/')
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    # NEW: The "No Room" Check
    if flight.seats_remaining <= 0:
        messages.error(request, "Sorry, this flight is already fully booked!")
        return redirect('home')
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user 
            booking.flight = flight
            booking.save()
            messages.success(request, f'Successfully booked flight to {flight.destination}!')
            return redirect('home')
    else:
        form = BookingForm()
    
    return render(request, 'flights/book_flight.html', {'form': form, 'flight': flight})

# This handles the "Read" part of the Custom Model
@login_required(login_url='/accounts/login/')
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'flights/my_bookings.html', {'bookings': bookings})

# Cancel booking view
@login_required(login_url='/accounts/login/')
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        booking.status = 'Cancelled'
        booking.save()
        messages.success(request, 'Booking successfully cancelled.')
        return redirect('my_bookings')
    
    return render(request, 'flights/cancel_confirm.html', {'booking': booking})

# Edit booking view
@login_required(login_url='/accounts/login/')
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, f'Booking for {booking.flight.destination} updated!')
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)
    
    return render(request, 'flights/edit_booking.html', {'form': form, 'booking': booking})

# NEW: Profile view added at the bottom
@login_required(login_url='/accounts/login/')
def profile_view(request):
    # This retrieves the profile created by your signal
    profile = request.user.profile 
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your travel profile has been updated!')
            return redirect('my_bookings')
    else:
        form = ProfileForm(instance=profile)
        
    return render(request, 'flights/profile.html', {'form': form})

from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent! We'll fly back to you soon.")
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'flights/contact.html', {'form': form})

# 1. DELETE: Completely removes the booking from the database
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking has been permanently deleted.')
        return redirect('my_bookings')
    return render(request, 'flights/delete_confirm.html', {'booking': booking})

# 2. REBOOK: Changes a 'Cancelled' status back to 'Confirmed'
@login_required
def rebook_flight(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    # Safety Check: Make sure there are still seats!
    if booking.flight.seats_remaining > 0:
        booking.status = 'Confirmed'
        booking.save()
        messages.success(request, f'Flight to {booking.flight.destination.city} is rebooked!')
    else:
        messages.error(request, 'Sorry, this flight is now sold out. Please pick a new one.')
        
    return redirect('my_bookings')
