from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.


def student(request):
    fm = StudentRegistration()
    return render(request, 'enroll/studentform.html', {'form': fm})
