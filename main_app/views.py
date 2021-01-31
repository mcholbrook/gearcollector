from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gear_index(request):
  return render(request, 'gear/index.html')