# Generated by Django 4.0.6 on 2022-07-28 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0003_measurement_user_alter_measurement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(default=datetime.date(2022, 7, 27)),
        ),
    ]