from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def alphanumeric(value):
    if not value.isalnum():
        raise ValidationError("Only alphanumeric characters are allowed.")
    return value

class carList(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=False)
    chasisNumber = models.CharField(max_length=100, null=True,validators=[alphanumeric])
    price=models.DecimalField(max_digits=10, decimal_places=2,default="0.00")

    def __str__(self):
        return self.name




class showroomList(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length = 100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
  

   