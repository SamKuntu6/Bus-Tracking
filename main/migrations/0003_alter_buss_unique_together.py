# Generated by Django 3.2.5 on 2022-06-23 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_trip_trip_ref_no'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='buss',
            unique_together={('plate_no', 'driver_assigned', 'attendant_assigned')},
        ),
    ]