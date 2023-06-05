from django.shortcuts import render


def index(request):
    context = {
        'title': 'title'
    }
    return render(request, 'home/index.html', context)


def home(request):
    return render (request, 'home/home.html')