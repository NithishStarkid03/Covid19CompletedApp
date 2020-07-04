from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
import random
import time
import string
import pandas as pd
import io
import requests

def home(request):
    if request.method=='POST':
        return redirect('/home')
    else:
      return render(request,'home.html')

def symptoms(request):
    if request.method=='POST':
        inp = request.POST['check']
        sym = inp.split(',')
        result = []
        if 'severe cough' in sym:
            result.append('Cough: Take medicines.  Stay in home.  Do not come out.')
        if 'cant breathe' in sym:
            result.append('Breathing problem: Its time you meet a doctor.  Go to the nearest government hosptial.')
        if 'fever' in sym:
            result.append('Fever: Ask someone in house to get prescriptions from doctor.  Eat medicines and stay in home')
        if 'cold' in sym:
            result.append('Cold: Probably it is normal cold.  So take some medicines and be safe.')
        messages.info(request,result)    
        return redirect('/symptoms')
    else:
        return render(request,'symptoms.html')

def status(request):
    url="https://api.covid19india.org/csv/latest/state_wise.csv"
    data = pd.read_csv(url)
    table = data.values.tolist()
    for i in range(len(table)):
        table[i] = table[i][:5]
    context={
        "table":table
    }
    return render(request,'status.html',context)

def contact(request):
    if request.method=='POST':
        return redirect('/contact')
    else:
        return render(request,'contact.html')
