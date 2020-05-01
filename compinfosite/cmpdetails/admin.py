
from django.contrib import admin

# Register your models here.

from .models import Company , Employee


class EmployeeAdmin(admin.TabularInline):
    model = Employee
    extra=1
    list_display = ('firs_name', 'last_name','salary', 'status')


class CompanyAdmin(admin.ModelAdmin):
    fields = ['comp_name','comp_budget']
    inlines = [EmployeeAdmin]
    list_display = ('comp_name','comp_budget')

admin.site.register(Company,CompanyAdmin)
