from django.contrib import admin
from .models import Airport, Flight, Booking, PassengerProfile
from .models import ContactMessage

# Register basic models
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(PassengerProfile)

# Advanced registration for Booking to show 'Status' in the list
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'passenger_name', 'status', 'created_at')
    list_filter = ('status', 'created_at')

# Register the Contact Message model
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # This shows the name, subject, and date in the list view
    list_display = ('name', 'subject', 'created_at')
    
    # This makes the messages "Read Only" so you don't accidentally edit a customer's message
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    
    # This adds a sidebar to filter by date
    list_filter = ('created_at',)

