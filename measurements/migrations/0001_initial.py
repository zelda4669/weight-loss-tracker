# Generated by Django 4.0.6 on 2022-07-25 03:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2022, 7, 25, 3, 12, 48, 298065, tzinfo=utc))),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bust', models.DecimalField(decimal_places=2, max_digits=6)),
                ('chest', models.DecimalField(decimal_places=2, max_digits=6)),
                ('waist', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hips', models.DecimalField(decimal_places=2, max_digits=6)),
                ('left_thigh', models.DecimalField(decimal_places=2, max_digits=6)),
                ('right_thigh', models.DecimalField(decimal_places=2, max_digits=6)),
                ('left_calf', models.DecimalField(decimal_places=2, max_digits=6)),
                ('right_calf', models.DecimalField(decimal_places=2, max_digits=6)),
                ('left_forearm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('right_forearm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('left_upper_arm', models.DecimalField(decimal_places=2, max_digits=6)),
                ('right_upper_arm', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]