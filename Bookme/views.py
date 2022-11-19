from django.http import HttpResponse
from django.views.generic import FormView
from django_tables2 import SingleTableView

from Bookme.forms import ReservationForm
from Bookme.models import Reservation
from Bookme.tables import RentalTable


class RentalsListView(SingleTableView):
    model = Reservation
    table_class = RentalTable
    template_name = 'Bookme/check_reservations.html'


class AddRentalView(FormView):
    template_name = 'Bookme/add_reservation.html'
    form_class = ReservationForm
    success_url = 'bookme/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    #TODO: Implement the invalid form


def success(request):
    return HttpResponse("Reservation successfully added.")
