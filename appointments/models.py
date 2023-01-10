from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.
class Appointments(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(null=False, blank=True)
    time  = models.TimeField(null=False, default='00:00:00')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    customer_name = models.CharField(null=False, blank=False, max_length=140)
    customer_last_name = models.CharField(null=False, blank=False, max_length=140)
    email = models.EmailField(null=False, blank=False, max_length=254)
    salon = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("appointment_home")
