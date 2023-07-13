from django.urls import path

from . import views

app_name = "gradebooks"

urlpatterns = [
     # Grade Book Management URLs
    path('gradebooks/', views.gradebook_list, name='gradebook_list'),
    path('gradebooks/<int:gradebook_id>/', views.gradebook_detail, name='gradebook_detail'),
    
]