from django.shortcuts import render
from home.models import Summary


def index(request):
    context = {
        'title': 'CVMaker',
        'summaries': Summary.objects.all(),
    }
    return render(request, 'home/index.html', context)


def home(request):
    return render(request, 'home/home.html')