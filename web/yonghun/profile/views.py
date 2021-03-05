from django.shortcuts import render

from ..models import Company


def index(request):
    company = Company.objects.all().order_by('start_date')

    context = {'company': company}
    return render(request, 'profile/index.html', context=context)

