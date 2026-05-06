from django.db import models

class Employee(models.Model):
    eid = models.IntegerField()
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.name