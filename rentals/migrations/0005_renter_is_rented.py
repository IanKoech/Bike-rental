# Generated by Django 3.1.6 on 2021-02-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='renter',
            name='is_rented',
            field=models.BooleanField(default=False),
        ),
    ]
