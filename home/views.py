from django.shortcuts import render
from home.forms import SummaryForm
from home.generator import convert
from home.models import Summary


def index(request):
    currentUserId = request.user.id

    summaries = Summary.objects.filter(user=currentUserId)

    context = {
        'title': 'CVMaker',
        'summaries': summaries,
    }
    return render(request, 'home/index.html', context)


def home(request):
    if request.method == 'POST':

        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        number = request.POST['number']
        education = request.POST['education']
        experience = request.POST['experience']
        skills = request.POST['skills']
        languages = request.POST['languages']

        Summary.objects.create(name='name', path='path', user=request.user.id)

        return convert(name, surname, email, number, education, experience, skills, languages)

    else:
        form = SummaryForm()
    context = {'form': form}
    return render(request, 'home/home.html', context)
