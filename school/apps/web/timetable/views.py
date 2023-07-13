from django.shortcuts import render

from .models import Timetable

# Timetable Management views
def timetable_list(request):
    timetables = Timetable.objects.all()
    return render(request, 'timetable_list.html', {'timetables': timetables})

def timetable_detail(request, timetable_id):
    timetable = Timetable.objects.get(pk=timetable_id)
    return render(request, 'timetable_detail.html', {'timetable': timetable})