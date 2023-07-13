from django.urls import path

from . import views

app_name = "library"

urlpatterns = [
    # Library Management URLs
    path('libraries/', views.library_list, name='library_list'),
    path('libraries/<int:library_id>/', views.library_detail, name="")
]