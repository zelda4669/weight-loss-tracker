from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import date


class Measurement(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateField(default=date.today())
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

    def get_absolute_url(self):
        return reverse('measurement_detail', kwargs={'pk': self.pk})