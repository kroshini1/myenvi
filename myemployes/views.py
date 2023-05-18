from django.shortcuts import render,redirect

from django.http import HttpResponse

from .models import employes
from .forms import EmployeeForm

# Create your views here.

def index(request):
    employees=employes.objects.all()
    return render(request,'myemployes/index.html',{'employees':employees})


def emp_details(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'myemployes/emp.html', {'form': form})
