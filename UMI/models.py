import random

from django.db import models

# Create your models here.
from accounts.models import Doctor, User


class Disease(models.Model):
    disease_id = models.BigAutoField(primary_key=True)
    disease_name = models.CharField(max_length=30)

    class Meta:
        ordering = ('disease_name',)

    def __str__(self):
        return self.disease_name


class Department(models.Model):
    department_id = models.BigAutoField(primary_key=True)
    department_name = models.CharField(max_length=50)

    class Meta:
        ordering = ('department_name',)

    def __str__(self):
        return self.department_name


class Appointment(models.Model):
    appointment_id = models.BigAutoField(primary_key=True)
    appointment_title = models.CharField(max_length=100)
    date = models.DateTimeField()
    #disease_name = models.ForeignKey(Disease, on_delete=models.CASCADE)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #patient_id = models.BigIntegerField(Patient.patient_id)
    content = models.CharField(max_length=500)
    #doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    class Meta:
        ordering = ('appointment_title',)

    def __str__(self):
        return self.appointment_title


class Report(models.Model):
    report_id = models.BigAutoField(primary_key=True)
    report_title = models.CharField(max_length=100)
    report_type = models.CharField(max_length=50)
    report_center = models.CharField(max_length=50)

    class Meta:
        ordering = ('report_title',)

    def __str__(self):
        return self.report_title


class Prescribtion(models.Model):
    prescribtion_id = models.BigAutoField(primary_key=True)
    prescribtion_content = models.CharField(max_length=500)

    class Meta:
        ordering = ('prescribtion_content',)

    def __str__(self):
        return self.prescribtion_content


class Duration(models.Model):
    duration = models.CharField(max_length=30)

    class Meta:
        ordering = ('duration',)

    def __str__(self):
        return self.duration


class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    blood_group = models.CharField(max_length=50)
    DOB = models.DateField() #staff also
    insurance_license_no = models. BigIntegerField(default=0)
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    # filled by staff
    current_docID = models.BigIntegerField(null=False)
    diseases = models.ManyToManyField(Disease)
    departments = models.ManyToManyField(Department)
    doctors = models.ManyToManyField(Doctor)
    appointments = models.ManyToManyField(Appointment)
    reports = models.ManyToManyField(Report)
    prescribtions = models.ManyToManyField(Prescribtion)
    durations = models.ManyToManyField(Duration)

    #def __str__(self):
    #    return self.patient_id

    def save(self):
        if not self.patient_id:
            is_Unique = False
            while not is_Unique:
                self.patient_id = random.randint(1000000000000000000, 1999999999999999999)
                is_Unique = (Patient.objects.filter(patient_id=self.patient_id).count() == 0)
        super(Patient, self).save()


class staff(models.Model):
    staff_ID = models.BigAutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    staff_name = models.CharField(max_length=50)
    DOB = models.DateField()
    blood_group = models.CharField(max_length=50)


    def __str__(self):
        return self.staff_ID

class insurance_company(models.Model):
    insurance_company_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    company_license = models.CharField(max_length=50)

    def __str__(self):
        return self.insurance_company_id
