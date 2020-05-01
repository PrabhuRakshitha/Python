from django.shortcuts import render

# Create your views here.


def myapps(request):
    return render(request,'Myapps.html')