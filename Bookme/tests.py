from django.test import TestCase
from Bookme.models import Reservation, Rental, InvalidDatesProvided


class ReservationTest(TestCase):

    def setUp(self):
        Rental.objects.create(name="test_rental")

    def test_checkout_post_checkin(self):
        """Checkout dates before checkin are invalid form data."""
        test_reservation = Reservation(associated_rental_name=Rental.objects.all()[0], checkin="2022-01-22", checkout="2022-01-21")
        try:
            test_reservation.save()
        except InvalidDatesProvided as e:
            self.assertIsInstance(e, InvalidDatesProvided)
 