from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Item, Trip
from .forms import NoteForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def gear_index(request):
  items = Item.objects.filter(user=request.user)
  return render(request, 'gear/index.html', {'items': items})

@login_required
def gear_detail(request, item_id):
  item = Item.objects.get(id=item_id)
  trips_gear_doesnt_have = Trip.objects.exclude(id__in = item.trips.all().values_list('id'))
  note_form = NoteForm()
  return render(request, 'gear/details.html', {'item': item, 'note_form': note_form, 'trips': trips_gear_doesnt_have})

@login_required
def add_note(request, item_id):
  form = NoteForm(request.POST)
  if form.is_valid():
    new_note = form.save(commit=False)
    new_note.item_id = item_id
    new_note.save()
  return redirect('gear_detail', item_id=item_id)

class ItemCreate(LoginRequiredMixin, CreateView):
  model = Item
  fields = ['name', 'description', 'category', 'typeofcamping']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Item
  fields = '__all__'

class ItemDelete(LoginRequiredMixin, DeleteView):
  model = Item
  success_url = '/gear/'

class TripList(LoginRequiredMixin, ListView):
  model = Trip

class TripDetail(LoginRequiredMixin, DetailView):
  model = Trip

class TripCreate(LoginRequiredMixin, CreateView):
  model = Trip
  fields = ['name', 'location']

class TripUpdate(LoginRequiredMixin, UpdateView):
  model = Trip
  fields = ['name', 'location']

class TripDelete(LoginRequiredMixin, DeleteView):
  model = Trip
  success_url = '/trips/'

@login_required
def assoc_trip(request, item_id, trip_id):
  Item.objects.get(id=item_id).trips.add(trip_id)
  return redirect('gear_detail', item_id=item_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('gear_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)