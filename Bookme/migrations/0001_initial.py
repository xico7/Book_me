# Generated by Django 4.1.3 on 2022-11-18 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('checkout', models.DateTimeField()),
                ('checkin', models.DateTimeField()),
                ('previous_reservation_id', models.IntegerField()),
                ('rental_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('associated_rental_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bookme.rental')),
            ],
        ),
    ]
