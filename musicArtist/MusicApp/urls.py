from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('music/',views.music,name='index'),
    path('music/brunomars/', views.brunomars, name='index'),
    path('music/shaggy/', views.shaggy, name='index'),
    path('music/sade/', views.sade, name='index'),
]
