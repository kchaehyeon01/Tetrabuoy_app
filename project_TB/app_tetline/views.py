from django.shortcuts import render, redirect
from .models import Tetline

# Create your views here.
def tetline_map(request):
    # 로직 작성 부분
    return render(request, 'tetline_map.html')

def tetline_list(request):
    lines = Tetline.objects.all()
    return render(request, 'tetline_list.html', {'lines': lines})

def tetline_add(request):
    if request.method == 'POST':
        print(request.POST)
        new_line = Tetline.objects.create(
            line_name = request.POST['line_name'],
            location = request.POST['location'],
            led_power = request.POST['led_power'],
            sound_power = request.POST['sound_power'],
        )
        return redirect('tetline_list')
    return render(request, 'tetline_add.html')


def tetline_detail(request, line_id):
    line = Tetline.objects.get(id=line_id)
    return render(request, 'tetline_detail.html', {'line': line})