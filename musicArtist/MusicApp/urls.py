
#imports the path to the views
from django.urls import path

from . import views


#these are the routes to the music artist

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music,name='index'),
    path('music/brunomars/', views.brunomars, name='index'),
    path('music/shaggy/', views.shaggy, name='index'),
    path('music/sade/', views.sade, name='index'),
]
