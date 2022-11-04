from django.db import models


# Create your models here.


class Details(models.Model):
    vehicle_number = models.CharField(max_length=50, unique=True)

    options = (
        ('Two Wheelers', 'Two Wheelers'),
        ('Three Wheelers', 'Three Wheelers'),
        ('Four Wheelers', 'Four Wheelers')
    )

    vehicle_type = models.CharField(max_length=50,choices=options,default='Two Wheelers')
    vehicle_model = models.CharField(max_length=50)
    vehicle_description = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_number
