from django.db import models
from django.urls import reverse

CAMPING = (
  ('C', 'Car Camping'),
  ('B', 'Backpacking')
)

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  category = models.CharField(max_length=100)
  notes = models.TextField(max_length=500)
  typeofcamping = models.CharField(
    max_length=1,
    choices=CAMPING,
    default=CAMPING[0][0]
  )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('gear_detail', kwargs={'item_id': self.id })