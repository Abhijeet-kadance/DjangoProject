from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Trainers(models.Model):
    trainer_name = models.CharField(max_length=200)
    trainer_age = models.PositiveIntegerField(blank=True,null=True)
    trainer_type = models.CharField(max_length=200)


    def __str__(self):
        return self.trainer_name