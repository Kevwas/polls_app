# Generated by Django 3.1.4 on 2021-01-30 08:17

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210130_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+12125552368', max_length=128, null=True, region=None),
        ),
    ]
