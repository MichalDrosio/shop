from django.contrib.auth.models import User
from django.db import models

direct = (
    (48,'Polska +48'),
    (1, 'USA +1'),
    (39, 'Włochy +39'),
)

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.PositiveIntegerField( null=True, blank=True)
    nr_selfphone = models.PositiveIntegerField(null=True, blank=True)
    direction_phone = models.PositiveIntegerField(choices=direct, null=True)