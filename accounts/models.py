from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)
    business_name = models.CharField(null=True, blank=True, max_length=500)
    first_name = models.CharField(null=True, blank=True, max_length=500)
    last_name = models.CharField(null=True, blank=True, max_length=500)

