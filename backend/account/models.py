from django.db import models

# Create your models here.
class UserRegister(models.Model):
        MALE = 'M'
        FEMALE = 'F'
        OTHER = 'O'

        GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
        username = models.CharField(max_length=30)
        email=models.EmailField(max_length=50)
        dateofbirth = models.DateTimeField()
        gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
        password = models.PasswordField()
        confirm_password = models.PasswordField()
        created_at = models.DateTimeField(auto_now_add=True)
        
        def __init__(self):
            self.username
            