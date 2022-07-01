from django.db import models

# Create your models here.
class Measurements(models.Model):
    date = models.DateField()
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    bust = models.DecimalField(max_digits=6, decimal_places=2)
    chest = models.DecimalField(max_digits=6, decimal_places=2)
    waist = models.DecimalField(max_digits=6, decimal_places=2)
    hips = models.DecimalField(max_digits=6, decimal_places=2)
    neck = models.DecimalField(max_digits=6, decimal_places=2)
    left_thigh = models.DecimalField(max_digits=6, decimal_places=2)
    left_calf = models.DecimalField(max_digits=6, decimal_places=2)
    left_forearm = models.DecimalField(max_digits=6, decimal_places=2)
    left_upper_arm = models.DecimalField(max_digits=6, decimal_places=2)
    right_thigh = models.DecimalField(max_digits=6, decimal_places=2)
    right_calf = models.DecimalField(max_digits=6, decimal_places=2)
    right_forearm = models.DecimalField(max_digits=6, decimal_places=2)
    right_upper_arm = models.DecimalField(max_digits=6, decimal_places=2)