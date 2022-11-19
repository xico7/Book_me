import django_tables2 as tables
from .models import Rental


class RentalTable(tables.Table):
    # TODO: Find a way to replace 0 in id with '-'
    class Meta:
        model = Rental
        template_name = "django_tables2/bootstrap.html"
        fields = ("associated_rental_name", "rental_id", "previous_reservation_id", "checkout", "checkin")