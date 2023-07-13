from django.urls import path, include


urlpatterns = [
    path('', include('school.apps.web.urls')),
]
