from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def passenger(request):
    return render(request,'pass.html')
