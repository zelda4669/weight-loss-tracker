from django.db import models
from django.utils import timezone

class Measurement(models.Model):
    date = models.DateField(default=timezone.now())
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    bust = models.DecimalField(max_digits=6, decimal_places=2)
    chest = models.DecimalField(max_digits=6, decimal_places=2)
    waist = models.DecimalField(max_digits=6, decimal_places=2)
    hips = models.DecimalField(max_digits=6, decimal_places=2)
    left_thigh = models.DecimalField(max_digits=6, decimal_places=2)
    right_thigh = models.DecimalField(max_digits=6, decimal_places=2)
    left_calf = models.DecimalField(max_digits=6, decimal_places=2)
    right_calf = models.DecimalField(max_digits=6, decimal_places=2)
    left_forearm = models.DecimalField(max_digits=6, decimal_places=2)
    right_forearm = models.DecimalField(max_digits=6, decimal_places=2)
    left_upper_arm = models.DecimalField(max_digits=6, decimal_places=2)
    right_upper_arm = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Body Comp from {self.date}'