from django.db import models


class InvalidDatesProvided(Exception): pass


class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class Rental(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Reservation(BaseModel):
    associated_rental_name = models.ForeignKey(Rental, on_delete=models.CASCADE)
    rental_id = models.IntegerField(default=0, primary_key=True)
    checkout = models.DateTimeField()
    checkin = models.DateTimeField()
    previous_reservation_id = models.IntegerField()

    def save(self, *args, **kwargs):
        rentals = {r['id']: r['name'] for r in [rental for rental in Rental.objects.all().values()]}

        rental_reservations_ids = []
        for reservation in Reservation.objects.all().values():
            if rentals[reservation['associated_rental_name_id']] == str(self.associated_rental_name):
                rental_reservations_ids.append(reservation['rental_id'])

        self.previous_reservation_id = max(rental_reservations_ids) if rental_reservations_ids else 0
        self.rental_id = self.previous_reservation_id + 1

        if self.checkout < self.checkin:
            raise InvalidDatesProvided("Dear customer, check in date must be before checkout.")

        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.rental_id)
