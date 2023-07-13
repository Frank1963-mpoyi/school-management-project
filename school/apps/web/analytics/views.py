from django.shortcuts import render

from .models import Analytics

# Analytics and Report Management views
def analytics_list(request):
    analytics = Analytics.objects.all()
    return render(request, 'analytics_list.html', {'analytics': analytics})

def analytics_detail(request, analytics_id):
    analytics = Analytics.objects.get(pk=analytics_id)
    return render(request, 'analytics_detail.html', {'analytics': analytics})
