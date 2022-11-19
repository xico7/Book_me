from django import forms

from Bookme.models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ('associated_rental_name', 'checkout', 'checkin')

        widgets = {
            'Rental Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Check in': forms.DateField(),
            'Check out': forms.DateField(),
        }