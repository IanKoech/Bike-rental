# Generated by Django 3.1.6 on 2021-02-04 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0005_renter_is_rented'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
