from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlightList.as_view(), name='home'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]