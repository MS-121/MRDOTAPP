from django.contrib import admin
from .models import *
from accounts.models import *
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Report)
admin.site.register(Disease)
admin.site.register(Duration)
admin.site.register(Prescribtion)
admin.site.register(Department)
admin.site.register(staff)
admin.site.register(insurance_company)