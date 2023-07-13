from django.shortcuts import render

from .models import Assignment

# Assignment Management views
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignment_list.html', {'assignments': assignments})

def assignment_detail(request, assignment_id):
    assignment = Assignment.objects.get(pk=assignment_id)
    return render(request, 'assignment_detail.html', {'assignment': assignment})
