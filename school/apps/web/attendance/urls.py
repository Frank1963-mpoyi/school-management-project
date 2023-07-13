from django.urls import path

from . import views

app_name = "attendance"

urlpatterns = [
      # Attendance Management URLs
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/<int:attendance_id>/', views.attendance_detail, name='attendance_detail'),

    
]