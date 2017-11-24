from django.shortcuts import render, redirect
from .forms import *
from .models import *

def add_a_customer(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'productdevelopment/add_a_customer.html')

def add_an_order():
    pass