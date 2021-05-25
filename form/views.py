from django.shortcuts import render
from form.forms import InputForm
from django.http import HttpResponse
import joblib
import numpy as np
from . import prediction

def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    if request.method == "POST":
        MyForm = InputForm(request.POST) 
        if MyForm.is_valid(): 
            try:
                data = MyForm.cleaned_data
                response = prediction.pred(**data)
            except Exception as e:
                return render(request, "index.html",{'errors':True})  
                      
        return render(request, 'results.html',{'response':response})
    else:
        return render(request, "index.html",{'form':MyForm})