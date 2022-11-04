from django.db import models
from django.core.validators import RegexValidator


# Create your models here.


class Details(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    alphabet = RegexValidator(r'^[a-zA-Z]*$', 'Only characters are allowed.')
    vehicle_number = models.CharField(max_length=50, unique=True, validators=[alphanumeric])

    options = (
        ('Two Wheelers', 'Two Wheelers'),
        ('Three Wheelers', 'Three Wheelers'),
        ('Four Wheelers', 'Four Wheelers')
    )

    vehicle_type = models.CharField(max_length=50,choices=options,default='Two Wheelers')
    vehicle_model = models.CharField(max_length=50,validators=[alphabet])
    vehicle_description = models.CharField(max_length=100,validators=[alphabet])

    def __str__(self):
        return self.vehicle_number
