from django.db import models

# Create your models here.

class BodyComposition(models.Model):
    date = models.DateTimeField()
    weight = models.FloatField()
    fat_mass = models.FloatField(blank=True, null=True)
    bone_mass = models.FloatField(blank=True, null=True)
    muscle_mass = models.FloatField(blank=True, null=True)
    hydration = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Date: {self.date} Weight: {self.weight}"