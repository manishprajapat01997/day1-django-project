from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def add_employee(request):

    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('show_url')

    template_name = 'app1/AddEmployee.html'
    context = {'form': form}

    return render(request, template_name, context)


def show_employee(request):

    data = Employee.objects.all()

    template_name = 'app1/ShowEmployee.html'
    context = {'data': data}

    return render(request, template_name, context)


def update_employee(request, pk):

    obj = Employee.objects.get(id=pk)

    form = EmployeeForm(instance=obj)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect('show_url')

    template_name = 'app1/AddEmployee.html'
    context = {'form': form}

    return render(request, template_name, context)


def delete_employee(request, pk):

    obj = Employee.objects.get(id=pk)
    obj.delete()

    return redirect('show_url')