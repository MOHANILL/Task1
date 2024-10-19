from django.db import models
from location.models import Location


class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " | " + str(self.capacity)