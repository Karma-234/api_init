from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phoneNumber = models.CharField(max_length=11, unique=True)
    userBio = models.CharField(max_length=50)
    profileImage = models.ImageField(upload_to="userProfile", null=True)
