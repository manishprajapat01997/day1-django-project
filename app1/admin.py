from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['id', 'eid', 'name', 'dob', 'email', 'city', 'salary']

    search_fields = ['name', 'email', 'city']

    list_filter = ['city']

    ordering = ['id']