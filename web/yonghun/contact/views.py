from django.shortcuts import render

from ..models import Company


def index(request):

    context = {}
    return render(request, 'contact/index.html', context=context)

