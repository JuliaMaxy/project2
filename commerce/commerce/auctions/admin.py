from django.contrib import admin
from .models import Listing, WatchList, Category, Bid, User
# Register your models here.
admin.site.register(Listing)
admin.site.register(WatchList)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(User)