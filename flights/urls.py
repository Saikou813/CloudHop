from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlightList.as_view(), name='home'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my-bookings/', views.booking_list, name='my_bookings'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]