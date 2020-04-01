from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'listings/listings.html')

def listings(request):
    return render(request, 'listings/listing.html')

def seacrh(request):
    return render(request, 'listings/search.html')