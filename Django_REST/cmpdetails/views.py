from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import Avg, Max, Min, Count, Sum
from django.shortcuts import render
from django.urls import reverse
import logging

from .models import Company, Employee

# Create your views here.
logger = logging.getLogger(__name__)
def index(request):
    return render(request,'cmpdetails/index.html')

def cmp_details(request):
    latest_company_list = Company.objects.order_by('-comp_id')
    context = {
        'latest_company_list': latest_company_list,
    }
    return render(request,'cmpdetails/cmp_details.html',context)

def emp_details(request , comp_id):
    emp_details_list = Employee.objects.filter(comp_id=comp_id,status='Active')

    if emp_details_list.exists():

        comp = Company.objects.get(comp_id=comp_id)
        emp_details_list = emp_details_list.filter(status='Active')
        agg_sal=emp_details_list.aggregate(Max('salary'),Min('salary'),Sum('salary'))

        max_sal = emp_details_list.filter(salary=agg_sal['salary__max'])
        min_sal = emp_details_list.filter(salary=agg_sal['salary__min'])
        op_cost = comp.comp_budget-agg_sal['salary__sum']
        emp_count = emp_details_list.aggregate(Count('emp_id'))
        emp_count = emp_count['emp_id__count']

        context={ 'emp_details_list':emp_details_list,'company':comp,'max_sal':max_sal,'min_sal':min_sal,'opt_cost':op_cost,'emp_count':emp_count,}
        return render(request,'cmpdetails/emp_details.html',context)
    else:
        latest_company_list = Company.objects.order_by('-comp_id')
        context = {
            'latest_company_list': latest_company_list,
            'error_message': "Active employees for the selected company does not exist",
        }
    return render(request, 'cmpdetails/cmp_details.html', context)


def emp_delete(request ,comp_id, emp_id):
    emp = Employee.objects.get(emp_id=emp_id)
    emp.status='Inactive'
    emp.save()
    return HttpResponseRedirect(reverse('cmpdetails:cmp_details'))


def emp_update(request, comp_id, emp_id):
    emp_list= Employee.objects.get(emp_id=emp_id)

    context= {'emp_list':emp_list,}
    return render(request, 'cmpdetails/emp_update.html', context)


def emp_update_save(request, emp_id):
    emp = Employee.objects.get(emp_id=emp_id)
    emp.first_name = request.POST['emp_fname']
    emp.last_name = request.POST['emp_lname']
    emp.salary = request.POST['emp_sal']
    emp.status = request.POST['emp_status']
    emp.save()
    return HttpResponseRedirect(reverse('cmpdetails:emp_details', args=(emp.comp_id.pk,)))

def add_new_emp_pg(request,comp_id):
    context={'comp_id':comp_id,}
    return render(request,'cmpdetails/emp_add_new.html',context)


def emp_add_new(request, comp_id):
    emp_fname = request.POST['emp_fname']
    emp_lname = request.POST['emp_lname']
    emp_sal = request.POST['emp_sal']
    emp_status = request.POST['emp_status']
    comp=Company.objects.get(comp_id=comp_id)
    emp=Employee(first_name=emp_fname, last_name=emp_lname, salary=emp_sal, status=emp_status,comp_id=comp)
    emp.save()
    return HttpResponseRedirect(reverse('cmpdetails:add_new_emp_pg', args=(comp_id,)))

