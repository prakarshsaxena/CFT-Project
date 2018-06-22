from django.shortcuts import render,redirect,HttpResponse
from . import models
from .models import Salary_calculations
from .forms import SalaryForm
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView,TemplateView
from django.contrib import messages

def salary_structure(request):
    context = Salary_calculations.objects.all()
    return render(request,'work/salary_struct_table.html',{'context':context})

def add(request):
    if request.method=="POST":
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/salary')
        else:
            return HttpResponse('Sorry! The salary_structure for this year has already been formed')
    else :
        form = SalaryForm()
        return render(request,'work/salary_struct_form.html',{'form':form})