from django.db import models

# Create your models here.

class UserProfile(models.Model): 
    
   # this is user personal profile so not available any one to edit except view and read only
   #getting first name and last name and email from the register model & and nickname as username as well but if only true
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address=models.CharField()
    job=models.CharField(max_length=20)
    sports=models.CharField(max_length=20, blank=True)
    hobby=models.CharField(max_length=20, blank=True)
    job=models.CharField(max_length=20, blank=True)
    mobile_number=models.CharField(max_length=20, blank=True)
    education=models.CharField(max_length=20, blank=True)
    country=models.CharField(max_length=20, blank=True)
    # photo featured
    # connections
    # friends/ followinggit  
    