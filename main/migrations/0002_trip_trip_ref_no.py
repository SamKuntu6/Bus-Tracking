# Generated by Django 3.2.5 on 2022-06-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='trip_ref_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
