# Generated by Django 3.1.4 on 2021-01-24 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210121_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
    ]
