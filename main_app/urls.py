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
]