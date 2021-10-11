import datetime

from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=250)
    course=models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
      return self.name