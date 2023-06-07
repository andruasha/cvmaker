from django.shortcuts import render
from home.models import Summary
from home.forms import SummaryForm
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas


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

        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        # Настройте документ PDF
        p.setFont("Helvetica", 12)
        p.drawString(100, 700, "Имя: {}".format(name))
        p.drawString(100, 680, "Email: {}".format(email))
        # ... добавьте другие данные резюме

        # Завершите и сохраните документ PDF
        p.showPage()
        p.save()

        # Получите содержимое PDF из буфера
        buffer.seek(0)
        pdf = buffer.getvalue()
        buffer.close()

        # Отправьте сгенерированный PDF в ответе HTTP
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        response.write(pdf)

        return response

    else:
        form = SummaryForm()
    context = {'form': form}
    return render(request, 'home/home.html', context)