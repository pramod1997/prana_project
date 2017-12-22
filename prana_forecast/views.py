# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse 

from .models import *
from .forms import *

from first import months_between , file_summary

from part_des import part_des

from plot_graph import plot_graph

from bestfit import bestfit




def model_form_upload(request): 
    


    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = Document.objects.all()[len(Document.objects.all())-1]
            return_dict=file_summary(obj.document.name)
            file_uploaded=return_dict.get('actual_file_name')
            # this one saves directly
            print return_dict
            para = True
            srange=return_dict.get('no_of_parts')
            
    else:
        form = DocumentForm()
        return_dict={}
        para=False
        srange=0

        
    return render(request, 'prana_forecast/model_form_upload.html',  {
        'form': form, 'para': para, 'return_dict': return_dict , 'range':range(1,srange+1), 
    })

def second(request): 

    path_value =   list((request.path).split('/'))

    list1 = [str(r) for r in path_value]
    print list1 
    #### 
    ### get the last value from the list and that serves as 
    part_no=list1[-1]
    

    ### got the part no 
    obj = Document.objects.all()[len(Document.objects.all())-1]
    uploaded_file = obj.document.name

    actual_file_name=uploaded_file.split('/')
    actual_file_name = [str(r) for r in actual_file_name]

    file_name_passed = actual_file_name[1]


    ### recently uploaded file name in Document model

    

    #### get thr file summary 


    return_part_dict=part_des(uploaded_file,part_no)
    print return_part_dict

    #### call the best fit forecast function 

    best_fit_dict= bestfit(file_name_passed) ### a dictionary returned 

    print best_fit_dict 

    #### use the values to plot a plot 
    #### specify output html file where u want to store the graph of best fit

    best_fit_plot_name = "best_fit_plot.html"

    plot_graph([1,2,3],[1,2,3],1,3,1,3,best_fit_plot_name)   #### pass the dictionary values here 

    ##### pass the values from best_fit_dict dictionary 





    #### for advance section in html file
    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            selected_method = form.cleaned_data.get('selected_method')
            print selected_method
    else:
        form = OptionForm()

    

    ##### create a multi form getting all the values 




    ##### for advance form map the entire value to 1 : holtwinter etc 

    ### for parameters store them in database holt winter data base and others 

    #### for plotting use the database value and plot the graphs using first.py ( create a separate file )  



    return render(request, 'prana_forecast/second.html',  {
        'return_part_dict':return_part_dict,
        'form':form 
    })

def third(request):



    if request.method == 'POST':
        form = AdvanceForm(request.POST)
        if form.is_valid():
            form.save()
            obj = Advance.objects.all()[len(Advance.objects.all())-1]
            
                        
    else:
        form = AdvanceForm()
        

        
    return render(request, 'prana_forecast/third.html',  {
        'form': form,  
    })




# Create your views here.
