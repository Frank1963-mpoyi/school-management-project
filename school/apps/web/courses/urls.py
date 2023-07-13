from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    # Course Management URLs
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),

    
]