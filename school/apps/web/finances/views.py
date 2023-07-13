from django.shortcuts import render

from .models import FinancialRecord

# Financial Management views
def financialrecord_list(request):
    financialrecords = FinancialRecord.objects.all()
    return render(request, 'financialrecord_list.html', {'financialrecords': financialrecords})

def financialrecord_detail(request, financialrecord_id):
    financialrecord = FinancialRecord.objects.get(pk=financialrecord_id)
    return render(request, 'financialrecord_detail.html', {'financialrecord': financialrecord})