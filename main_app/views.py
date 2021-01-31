from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gear_index(request):
  items = Item.objects.all()
  return render(request, 'gear/index.html', {'items': items})

def gear_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  return render(request, 'gear/details.html', {'item': item})

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/gear/'