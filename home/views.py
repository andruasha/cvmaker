from django.shortcuts import render
from home.models import Summary
from home.forms import SummaryForm
from home.generator import pdfGenerate


def index(request):
    context = {
        'title': 'CVMaker',
        'summaries': Summary.objects.all(),
    }
    return render(request, 'home/index.html', context)


def home(request):
    if request.method == 'POST':
        form = SummaryForm(data=request.POST)

        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        number = request.POST['number']
        education = request.POST['education']
        experience = request.POST['experience']
        skills = request.POST['skills']
        languages = request.POST['languages']

        return pdfGenerate(name, surname, email, number, education, experience, skills, languages)

    else:
        form = SummaryForm()
    context = {'form': form}
    return render(request, 'home/home.html', context)
