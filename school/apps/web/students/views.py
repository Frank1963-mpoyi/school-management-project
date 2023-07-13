from django.shortcuts import render

from .models import Student

# Student Management views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'student_detail.html', {'student': student})