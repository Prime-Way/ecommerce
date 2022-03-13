from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    # ct = categ.objects.all()
    prod = product.objects.all()
    return render(request, 'home.html', {'pr': prod})
