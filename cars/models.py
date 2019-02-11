from django.db import models

# Create your models here.
class Car(models.Model):
    plate_num = models.CharField(max_length=6)
    owner = models.CharField(max_length=100)
    model = models.CharField(max_length=100) 
    def __str__(self):
        return self.plate_num
