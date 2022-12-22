from django.shortcuts import render, redirect, reverse
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.db.models.deletion import ProtectedError
from django.core.paginator import Paginator
from django.shortcuts import render


def index(request):
    return render(request, 'restaurant_app/index.html')

def menu(request):
    food = Food.objects.all()
    paginator = Paginator(food, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurant_app/menu.html',{'page_obj': page_obj})

def table(request):
    return render(request, 'restaurant_app/table.html')

def about_us(request):
    cookers = Cookers.objects.all()
    return render(request, 'restaurant_app/about_us.html', {'cookers' : cookers})

def feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'restaurant_app/feedback.html', {'feedback':feedback})

def create_feedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        feedback.first_name = request.POST.get('first_name')
        feedback.last_name = request.POST.get('last_name')
        feedback.email = request.POST.get('email')
        feedback.message = request.POST.get('message')
        feedback.phone = request.POST.get('phone')
        feedback.save()
    return redirect('index')
