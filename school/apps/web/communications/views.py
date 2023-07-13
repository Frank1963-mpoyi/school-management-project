from django.shortcuts import render

from .models import Communication

# Communication Management views
def communication_list(request):
    communications = Communication.objects.all()
    return render(request, 'communication_list.html', {'communications': communications})

def communication_detail(request, communication_id):
    communication = Communication.objects.get(pk=communication_id)
    return render(request, 'communication_detail.html', {'communication': communication})