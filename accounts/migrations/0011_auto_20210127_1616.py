# Generated by Django 3.1.4 on 2021-01-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='Bio', max_length=500, null=True),
        ),
    ]