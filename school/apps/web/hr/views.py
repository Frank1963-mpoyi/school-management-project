from django.shortcuts import render

from .models import HR

# Human Resource Management views
def hr_list(request):
    hr = HR.objects.all()
    return render(request, 'hr_list.html', {'hr': hr})

def hr_detail(request, hr_id):
    hr = HR.objects.get(pk=hr_id)
    return render(request, 'hr_detail.html', {'hr': hr})