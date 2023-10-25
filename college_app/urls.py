from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('college/<str:pk>/', views.viewCollege, name='college'),
    path('iit-bombay', views.iitbombay, name='iit-bombay'),
    path('vitbhopal', views.vitbhopal, name='vitbhopal'),
    path('iit-delhi', views.iitdelhi, name='iit-delhi'),
    path('iit-dhanbad', views.iitdhanbad, name='iit-dhanbad'),
    path('iit-goa', views.iitgoa, name='iit-goa'),
    path('vitchennai', views.vitchennai, name='vitchennai'),
    path('iit-gandhinagar', views.iitgandhinagar, name='iit-gandhinagar'),
    path('iit-guwahati', views.iitguwahati, name='iit-guwahati'),
    path('iit-roorkee', views.iitroorkee, name='iit-roorkee'),
    path('iit-jodhpur', views.iitjodhpur, name='iit-jodhpur'),
    path('iit-kanpur', views.iitkanpur, name='iit-kanpur'),
    path('iit-patna', views.iitpatna, name='iit-patna'),
    path('nirf-ranking', views.nirfranking, name='nirf-ranking'),
    path('vitvellore', views.vitvellore, name='vitvellore'),
    path('vitamaravati', views.vitamaravati, name='vitamaravati'),
    path('about', views.about, name='about'),
]
