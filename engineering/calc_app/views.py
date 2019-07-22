from django.shortcuts import render
from calc_app.forms import RectangleForm, FanUnbalanceForm
from lib.rectangle_properties import Rect
from lib.fan_unbalance import Fan
from . models import Rectangle, FanUnbalance

# Create your views here.
def index(request):
    return render(request, 'index.html')

def rectangle(request):

    form = RectangleForm()

    if request.method == 'POST':
        form = RectangleForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            x=float(form.cleaned_data['rec_width'])
            y=float(form.cleaned_data['rec_height'])

            arta =Rect(x,y)
            result1 = arta.area()
            result2 = round(arta.p_moment(),2)

            return render(request, 'section_prop.html', {'form':form, 'result1':result1, 'result2':result2})
        else:
            print('Form Invalid')
    
    return render(request,'section_prop.html',{'form':form})

def fan_unbalance(request):
    form = FanUnbalanceForm()

    if request.method == 'POST':
        form = FanUnbalanceForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            A=float(form.cleaned_data['balance_grade'])
            B=float(form.cleaned_data['impeller_mass'])
            C=float(form.cleaned_data['fan_speed'])
            D=float(form.cleaned_data['backplate_dia'])

            fan =Fan(A,B,C,D)
            result1 = fan.pru()
            result2 = fan.patch_area()

            return render(request, 'fan_unbalance.html', {'form':form, 'result1':result1, 'result2':result2})
        else:
            print('Form Invalid')
    
    return render(request,'fan_unbalance.html',{'form':form})


