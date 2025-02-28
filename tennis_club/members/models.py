from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    phone_number = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

