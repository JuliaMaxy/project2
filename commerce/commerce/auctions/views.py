from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Listing, WatchList, Category ,Bid


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'listings': listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def new(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            categories = Category.objects.all()
            return render(request, "auctions/new.html", {
                "categories": categories
            })
        else:
                title = request.POST["title"]
                description = request.POST["description"]
                category = request.POST["category"]
                category = Category.objects.get(pk=category)
                condition = request.POST["condition"]
                bid = int(request.POST["bid"])
                image = request.FILES["img"]
                user = request.user
                listing = Listing(title=title, description=description, category=category, condition=condition, starting_bid=bid,
                                creator=user, picture=image)
                listing.save()
                return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))


@login_required
def listing(request, listing_id):
    user = request.user
    listing =  Listing.objects.get(pk=listing_id)
    in_watchlist = WatchList.objects.filter(user=user, listing=listing).exists()
    w = WatchList.objects.filter(listing=listing)
    watchers = 0
    for watcher in w:
        watchers += 1
    if request.method == 'GET':
        if in_watchlist:
            return render(request, "auctions/listing.html", {
                "listing":listing, "in_watchlist": True, "watchers":watchers
            })
        else:
            return render(request, "auctions/listing.html", {
                "listing":listing, "in_watchlist": False, "watchers":watchers
            })
    else:
        if request.POST["form"] == "1":
            listing_id = request.POST["add_listing"]
            listing = Listing.objects.get(pk=listing_id)
            addition = WatchList.objects.create(listing=listing)
            addition.user.add(user)
        elif request.POST["form"] == "2":
            bid = request.POST["bid"]
            bidded = Bid.objects.filter(listing=listing).exists()
            if not bidded:
                if int(bid) > listing.starting_bid:
                    b = Bid.objects.create(listing=listing, amount=bid)
                    b.user.add(user)
                    return render(request, "auctions/listing.html", {
                        "listing":listing, "in_watchlist": True, "watchers":watchers, "message":"Success"
                    })
            else:
                last =  Bid.objects.filter(listing=listing).order_by('added_time').first()
                if int(bid)> last.amount:
                    b = Bid.objects.create(listing=listing, amount=bid)
                    b.user.add(user)
                    return render(request, "auctions/listing.html", {
                        "listing":listing, "in_watchlist": True, "watchers":watchers, "message":"Success"
                    })
            
            return render(request, "auctions/listing.html", {
                "listing":listing, "in_watchlist": True, "watchers":watchers, "message":"Failed"
            })
    w = WatchList.objects.filter(listing=listing)
    watchers = 0
    for watcher in w:
        watchers += 1 
    return render(request, "auctions/listing.html", {
                "listing":listing, "in_watchlist": True, "watchers":watchers
            })

@login_required   
def watchlist(request):
    if request.method == "GET":
        user = request.user
        watchlist = user.watchlist.all()
        listings = []
        for listing in watchlist:
            listings.append(listing.listing)

        print(listings)
        return render(request, "auctions/watchlist.html", {
            "listings":listings})
    else:
        user = request.user
        listing_id = request.POST["delete_listing"]
        listing = Listing.objects.get(pk=listing_id)
        deletion= user.watchlist.get(listing=listing)
        deletion.delete()
        w = WatchList.objects.filter(listing=listing)
        watchers = 0
        for watcher in w:
            watchers += 1
        return render(request, "auctions/listing.html", {
                "listing":listing, "in_watchlist": False, "watchers":watchers
            })


@login_required
def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories":categories
    })

@login_required
def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    listings = category.listings.all()
    return render(request, "auctions/category.html", {
        "listings":listings, "category": category
    })