# Generated by Django 3.1.4 on 2021-03-15 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20210204_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
