from django.urls import path

from . import views

app_name = "timetable"

urlpatterns = [
     # Timetable Management URLs
    path('timetables/', views.timetable_list, name='timetable_list'),
    path('timetables/<int:timetable_id>/', views.timetable_detail, name='timetable_detail'),

    
]