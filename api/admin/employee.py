from django.contrib import admin
from api.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'email',  'position', 'hire_date')