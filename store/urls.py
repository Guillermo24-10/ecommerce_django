from TiendaOnline import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name='store'),
    
] 
