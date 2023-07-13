from django.shortcuts import render

from .models import Parent

# Parent Portal Management views
def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'parent_list.html', {'parents': parents})

def parent_detail(request, parent_id):
    parent = Parent.objects.get(pk=parent_id)
    return render(request, 'parent_detail.html', {'parent': parent})