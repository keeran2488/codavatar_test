from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username} - {self.first_name}'
