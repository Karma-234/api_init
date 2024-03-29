from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserRecipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    images = models.ImageField(upload_to="userRecipe")
    cookingDate = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Favorite (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, unique=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ForeignKey(
        UserRecipe, on_delete=models.CASCADE, related_name='image',)


class OtherUser(models.Model):
    name = models.CharField(max_length=254)
    streetName = models.TextField(),
    email = models.EmailField(unique=True)
    state = models.TextField()
    country = models.TextField()
    profileImage = models.ImageField(upload_to="userImage", null=True)
    age = models.IntegerField(null=True, blank=True, default=18)

    def __str__(self) -> str:
        return self.name
