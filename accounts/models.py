from django.db import models
from UMI.models import *

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    userType = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default=1234)
    lastLogin = models.DateTimeField()

    def __str__(self):
        return self.username


class Doctor(models.Model):
    doctor_id = models.BigAutoField(primary_key=True)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=50)
    doc_department = models.CharField(max_length=50)
    license_no = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=100)
    #current_appointmentID = models.ForeignKey(Appointment, related_name='appointment_id', null=False)

    class Meta:
        ordering = ('doctor_name',)

    def __str__(self):
        return self.doctor_name

