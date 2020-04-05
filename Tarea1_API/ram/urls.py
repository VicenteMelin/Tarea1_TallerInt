from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('location/<int:location_id>/', views.location, name='place'),
    path('character/<int:character_id>/', views.character, name='character'),
    path('episode/<int:episode_id>/', views.episode, name='episode'),
]