from django.test import TestCase
from Bookme.models import Reservation, Rental


class ReservationTest(TestCase):

    def setUp(self):
        Rental.objects.create(name="test_rental")

    def test_checkout_post_checkin(self):
        """Checkout dates before checkin are invalid form data."""
        test_reservation = Reservation(associated_rental_name=Rental.objects.all()[0], checkin="2022-01-20", checkout="2022-01-21")
        test_reservation.save()
