from django.contrib import admin
from testapp.models import Employee
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','salary','age']


admin.site.register(Employee,EmployeeAdmin)