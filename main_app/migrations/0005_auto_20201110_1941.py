# Generated by Django 3.1.3 on 2020-11-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='delivery_address',
            new_name='address',
        ),
    ]
