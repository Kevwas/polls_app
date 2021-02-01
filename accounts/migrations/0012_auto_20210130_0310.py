# Generated by Django 3.1.4 on 2021-01-30 08:10

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210127_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+55555555555', max_length=128, null=True, region=None),
        ),
    ]