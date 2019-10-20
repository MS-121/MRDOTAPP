from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'UMI/home.html')

def doctor(request):
    return render(request, 'UMI/doctor.html')

def insurance(request):
    return render(request, 'UMI/insurance.html')

def staff(request):
    return render(request, 'UMI/staff.html')

def profile(request):
    return render(request, 'UMI/profile.html')

def patient(request):
    return render(request, 'UMI/patient.html')
