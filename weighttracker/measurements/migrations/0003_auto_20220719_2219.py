# Generated by Django 3.1.8 on 2022-07-20 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_remove_measurements_neck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='date',
            field=models.DateField(default=datetime.date(2022, 7, 19)),
        ),
    ]
