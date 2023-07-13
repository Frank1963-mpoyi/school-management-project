from django.urls import path

from . import views

app_name = "finances"

urlpatterns = [
     # Financial Management URLs
    path('financialrecords/', views.financialrecord_list, name='financialrecord_list'),
    path('financialrecords/<int:financialrecord_id>/', views.financialrecord_detail, name='financialrecord_detail'),

    
]