from django.shortcuts import render
from django.views.generic import ListView
from testapp.models import Employee
# Create your views here.
class EmployeeListView(ListView):
    model = Employee
    template_name = 'testapp/employee_list.html'