from django.shortcuts import render

from .models import Library

# Library Management views
def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library_list.html', {'libraries': libraries})

def library_detail(request, library_id):
    library = Library.objects.get(pk=library_id)
    return render(request, 'library_detail.html', {'library': library})