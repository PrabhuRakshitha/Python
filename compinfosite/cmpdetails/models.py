from django.db import models

# Create your models here.


class Company(models.Model):
    comp_id = models.AutoField(primary_key=True)
    comp_name = models.CharField(max_length=100)
    comp_budget = models.IntegerField(default=0)


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    comp_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    salary = models.IntegerField(default=0)
    status = models.CharField(max_length=10)
