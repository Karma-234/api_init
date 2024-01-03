from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)
    file = models.FileField()
    streetName = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)
    key = models.UUIDField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Account(models.Model):
        accountNumber = models.IntegerField(default=1234567890)
        pass
