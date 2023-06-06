from django.contrib import admin
from .models import Listing, WatchList, Category
# Register your models here.
admin.site.register(Listing)
admin.site.register(WatchList)
admin.site.register(Category)