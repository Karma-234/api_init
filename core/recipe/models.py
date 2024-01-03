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
