from django.shortcuts import render
from .forms import employeeForm
from django.shortcuts import redirect
# Create your views here.


def employee_login(request):
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = employeeForm()
    return render(request, 'form/employee_login.html',{'form': form})


