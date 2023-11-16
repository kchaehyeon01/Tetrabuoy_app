from django.shortcuts import render, redirect
from .models import Supervisor

# Create your views here.

def settings_main(request):
    return render(request, 'settings_main.html')
    
def settings_init(request):
    if request.method == 'POST':
        print(request.POST)
        spvsr_init = Supervisor.objects.create(
            spvsr_name = request.POST['spvsr_name'],
            spvsr_id = request.POST['spvsr_id'],
            spvsr_onduty= request.POST['spvsr_onduty']=='on',
            spvsr_port= request.POST['spvsr_port'],

            spvsr_dutytime_start= request.POST['spvsr_dutytime_start'],
            spvsr_dutytime_end= request.POST['spvsr_dutytime_end'],

            spvsr_duty_mon=request.POST['spvsr_duty_mon']=='on',
            spvsr_duty_tue=request.POST['spvsr_duty_tue']=='on',
            spvsr_duty_wed=request.POST['spvsr_duty_wed']=='on',
            spvsr_duty_thu=request.POST['spvsr_duty_thu']=='on',
            spvsr_duty_fri=request.POST['spvsr_duty_fri']=='on',
            spvsr_duty_sat=request.POST['spvsr_duty_sat']=='on',
            spvsr_duty_sun= request.POST['spvsr_duty_sun']=='on',
        )
        return redirect('settings_main')
    return render(request, 'settings_init.html')