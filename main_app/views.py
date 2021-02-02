from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item, Trip
from .forms import NoteForm
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
  trips_gear_doesnt_have = Trip.objects.exclude(id__in = item.trips.all().values_list('id'))
  note_form = NoteForm()
  return render(request, 'gear/details.html', {'item': item, 'note_form': note_form, 'trips': trips_gear_doesnt_have})

def add_note(request, item_id):
  form = NoteForm(request.POST)
  if form.is_valid():
    new_note = form.save(commit=False)
    new_note.item_id = item_id
    new_note.save()
  return redirect('gear_detail', item_id=item_id)

class ItemCreate(CreateView):
  model = Item
  fields = ['name', 'description', 'category', 'typeofcamping']

class ItemUpdate(UpdateView):
  model = Item
  fields = '__all__'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/gear/'

class TripList(ListView):
  model = Trip

class TripDetail(DetailView):
  model = Trip

class TripCreate(CreateView):
  model = Trip
  fields = ['name', 'location']

class TripUpdate(UpdateView):
  model = Trip
  fields = ['name', 'location']

class TripDelete(DeleteView):
  model = Trip
  success_url = '/trips/'

def assoc_trip(request, item_id, trip_id):
  Item.objects.get(id=item_id).trips.add(trip_id)
  return redirect('gear_detail', item_id=item_id)