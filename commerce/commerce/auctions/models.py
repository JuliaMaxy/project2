from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    default_auto_field = 'django.db.models.BigAutoField'
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    starting_bid = models.IntegerField()
    picture = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"