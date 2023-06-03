from django.shortcuts import render


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'index.html', context)
