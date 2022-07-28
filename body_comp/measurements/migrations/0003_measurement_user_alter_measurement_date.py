# Generated by Django 4.0.6 on 2022-07-28 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('measurements', '0002_alter_measurement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]