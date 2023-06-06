from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class WatchList(models.Model):
    user = models.ManyToManyField(User,related_name="watchlist")
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="watchlisted")
    added_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.listing}"

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title}"

class Listing(models.Model):
    default_auto_field = 'django.db.models.BigAutoField'
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    starting_bid = models.IntegerField()
    picture = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")
    condition = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    