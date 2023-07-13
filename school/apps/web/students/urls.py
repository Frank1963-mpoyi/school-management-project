from django.urls import path

from . import views

app_name = "students"

urlpatterns = [
     # Student Management URLs
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    
]