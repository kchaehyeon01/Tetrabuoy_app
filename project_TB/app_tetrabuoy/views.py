from django.shortcuts import render, redirect
from .models import Tetrabuoy

# Create your views here.

def start(request):
    return render(request, 'start.html')

def tetrabuoy_map(request):
    return render(request, 'tetrabuoy_map.html')

def tetrabuoy_list(request):
    buoys = Tetrabuoy.objects.all()
    return render(request, 'tetrabuoy_list.html', {'buoys': buoys})

def tetrabuoy_map(request):
    buoys = Tetrabuoy.objects.all()
    return render(request, 'tetrabuoy_map.html', {'buoys': buoys})

def tetrabuoy_add(request):
    if request.method == 'POST':
        print(request.POST)
        new_buoy = Tetrabuoy.objects.create(
            buoy_name = request.POST['buoy_name'],
            location = request.POST['location'],
            battery_remain = request.POST['battery_remain'],
            led_power = request.POST['led_power']
        )
        return redirect('tetrabuoy_list')
    return render(request, 'tetrabuoy_add.html')

def tetrabuoy_detail(request, buoy_id):
    buoy = Tetrabuoy.objects.get(id=buoy_id)
    return render(request, 'tetrabuoy_detail.html', {'buoy': buoy})

def tetrabuoy_edit(request, buoy_id):
    buoy = Tetrabuoy.objects.get(id=buoy_id)
    if request.method == 'POST':
        Tetrabuoy.objects.filter(id=buoy_id).update(
            buoy_name=request.POST['buoy_name'],
            location=request.POST['location'],
            battery_remain=request.POST['battery_remain'],
            led_power=request.POST['led_power'],
        )
        return redirect('tetrabuoy_detail', buoy_id)
    return render(request, 'tetrabuoy_edit.html', {'buoy': buoy})
    
def tetrabuoy_delete(request, buoy_id):
    buoy = Tetrabuoy.objects.get(id=buoy_id)
    buoy.delete()
    return redirect('tetrabuoy_list')