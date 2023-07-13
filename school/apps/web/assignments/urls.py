from django.urls import path

from . import views

app_name = "assignments"

urlpatterns = [
     # Assignment Management URLs
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    
]