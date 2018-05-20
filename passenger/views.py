from django.shortcuts import render
from django.http  import HttpResponse
from .models import Passenger, Location, Reviews
# Create your views here.
def passenger(request):
    return render(request,'pass.html')
