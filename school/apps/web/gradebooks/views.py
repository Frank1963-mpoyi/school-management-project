from django.shortcuts import render

from .models import GradeBook

# Grade Book Management views
def gradebook_list(request):
    gradebooks = GradeBook.objects.all()
    return render(request, 'gradebook_list.html', {'gradebooks': gradebooks})

def gradebook_detail(request, gradebook_id):
    gradebook = GradeBook.objects.get(pk=gradebook_id)
    return render(request, 'gradebook_detail.html', {'gradebook': gradebook})
