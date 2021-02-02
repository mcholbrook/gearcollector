from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('gear/', views.gear_index, name='gear_index'),
  path('gear/<int:item_id>/', views.gear_detail, name='gear_detail'),
  path('gear/create/', views.ItemCreate.as_view(), name='gear_create'),
  path('gear/<int:pk>/update/', views.ItemUpdate.as_view(), name='gear_update'),
  path('gear/<int:pk>/delete/', views.ItemDelete.as_view(), name='gear_delete'),
  path('gear/<int:item_id>/add_note', views.add_note, name='add_note'),
  path('trips/', views.TripList.as_view(), name='trips_index'),
  path('trips/<int:pk>/', views.TripDetail.as_view(), name='trips_detail'),
  path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
  path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
  path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
  path('gear/<int:item_id>/assoc_trip/<int:trip_id>/', views.assoc_trip, name='assoc_trip'),
]