from django.shortcuts import render
from .models import Listing


# Create your views here.

def index(request):
    listings = Listing.objects.all()

    context = { 
        'listings' : listings
    }

def listings(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')