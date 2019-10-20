#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="HomePage"),
    path('doctor/', views.doctor, name="DocPage"),
    path('insurance/', views.insurance, name="InsurancePage"),
    path('staff/', views.staff, name="StaffPage"),
    path('profile/', views.profile, name="ProfilePage"),
    path('patient/', views.patient, name="PatientPage"),
]
