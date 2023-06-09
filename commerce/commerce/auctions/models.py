from django.contrib.auth.models import AbstractUser
from django.db import models
from decimal import Decimal


class User(AbstractUser):
    pass

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="bids")
    added_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.listing}-{self.amount}"


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
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    active = models.BooleanField(default=True)
    picture = models.ImageField(null=True, blank=True, upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")
    condition = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL,default=None, blank=True, null=True, related_name="won")
    closed_time = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
    