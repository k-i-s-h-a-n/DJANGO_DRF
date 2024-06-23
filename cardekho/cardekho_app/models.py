from django.db import models

# Create your models here.


class carList(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=False)
    chasisNumber = models.CharField(max_length=100, null=True,default="N/A")
    price=models.DecimalField(max_digits=10, decimal_places=2,default="0.00")

    def __str__(self):
        return self.name



