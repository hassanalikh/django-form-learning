from django.shortcuts import render
from .forms import StudentRegister

# Create your views here.


def studentReg(request):
    fm = StudentRegister()
    return render(request, 'enroll/studentform.html', {'form': fm})
