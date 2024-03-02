from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=22, blank=True)
    sports = models.CharField(max_length=20, blank=True)
    hobby = models.CharField(max_length=20, blank=True)
    job = models.CharField(max_length=20, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)
    education = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username # pylint: disable=no-member
    