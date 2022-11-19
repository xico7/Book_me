from django.urls import path

from .views import RentalsListView, AddRentalView, success

urlpatterns = [
    path('add_reservation/', AddRentalView.as_view()),
    path('add_reservation/bookme/success/', success),
    path('bookings/', RentalsListView.as_view()),
]
