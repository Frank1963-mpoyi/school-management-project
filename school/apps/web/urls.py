from django.urls import path, include


app_name = "web"

urlpatterns = [
    path('', include('school.apps.web.accounts.urls')),
    path('analytics/', include('school.apps.web.analytics.urls')),
    path('assignments/', include('school.apps.web.assignments.urls')),
    path('attendance/', include('school.apps.web.attendance.urls')),
    path('communications/', include('school.apps.web.communications.urls')),
    path('courses/', include('school.apps.web.courses.urls')),
    path('finances/', include('school.apps.web.finances.urls')),
    path('gradebooks/', include('school.apps.web.gradebooks.urls')),
    path('hr/', include('school.apps.web.hr.urls')),
    path('library/', include('school.apps.web.library.urls')),
    path('parents/', include('school.apps.web.parents.urls')),
    path('staff/', include('school.apps.web.staff.urls')),
    path('students/', include('school.apps.web.students.urls')),
    path('timetable/', include('school.apps.web.timetable.urls')),
]
