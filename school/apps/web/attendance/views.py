from django.shortcuts import render

from .models import Attendance

# Create your views here.
def attendance_list(request):
    attendance = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance': attendance})

def attendance_detail(request, attendance_id):
    attendance = Attendance.objects.get(pk=attendance_id)
    return render(request, 'attendance_detail.html', {'attendance': attendance})
