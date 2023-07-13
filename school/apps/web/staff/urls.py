from django.urls import path

from . import views

app_name = "staff"

urlpatterns = [
      # Staff Management URLs
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:staff_id>/', views.staff_detail, name='staff_detail'),

    
]