from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goats', views.goats, name='goats') 
]
