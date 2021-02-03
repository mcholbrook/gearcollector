from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CAMPING = (
  ('C', 'Car Camping'),
  ('B', 'Backpacking')
)

class Trip(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('trips_detail', kwargs={'pk': self.id})

class Item(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  category = models.CharField(max_length=100)
  typeofcamping = models.CharField(
    max_length=1,
    choices=CAMPING,
    default=CAMPING[0][0]
  )
  trips = models.ManyToManyField(Trip)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('gear_detail', kwargs={'item_id': self.id })

class Note(models.Model):
  date = models.DateField()
  content = models.TextField(max_length=500)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.content} on {self.date}"

  