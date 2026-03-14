from django.contrib import admin
from .models import Airport, Flight, Booking, PassengerProfile

# Register basic models
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(PassengerProfile)

# Advanced registration for Booking to show 'Status' in the list
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'passenger_name', 'status', 'created_at')
    list_filter = ('status', 'created_at')
