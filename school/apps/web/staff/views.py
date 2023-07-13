from django.shortcuts import render

from .models import Staff

# Staff Management views
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff': staff})

def staff_detail(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    return render(request, 'staff_detail.html', {'staff': staff})