from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import re
import os


def dataToPDF(name, surname, email, number, education, experience, skills, languages):

        fontPath = os.path.join(os.path.dirname(__file__), 'fonts/arial.ttf')
        pdfmetrics.registerFont(TTFont('Arial', fontPath))

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

        p = canvas.Canvas(response)

        p.setFont("Arial", 18)
        p.drawCentredString(300, 800, f"{surname} {name}")

        p.setFont("Arial", 14)
        p.drawCentredString(300, 780, email)
        p.drawCentredString(300, 760, number)

        p.setFont("Arial", 18)
        p.drawString(50, 680, "Образование")
        p.line(50, 670, 550, 670)
        p.setFont("Arial", 12)
        y = 650
        lines = re.split(r'[\r\n]+', education)
        for line in lines:
            p.drawString(50, y, "• " + line)
            y -= 15
        y = y - 20

        p.setFont("Arial", 18)
        p.drawString(50, y, "Опыт работы")
        p.line(50, y-10, 550, y-10)
        y = y - 30
        p.setFont("Arial", 12)
        lines = re.split(r'[\r\n]+', experience)
        for line in lines:
            p.drawString(50, y, "• " + line)
            y -= 15
        y = y - 20

        p.setFont("Arial", 18)
        p.drawString(50, y, "Профессиональные навыки")
        p.line(50, y-10, 550, y-10)
        y = y - 30
        p.setFont("Arial", 12)
        lines = re.split(r'[\r\n]+', skills)
        for line in lines:
            p.drawString(50, y, "• " + line)
            y -= 15
        y = y - 20

        p.setFont("Arial", 18)
        p.drawString(50, y, "Знание языков")
        p.line(50, y-10, 550, y-10)
        y = y - 30
        p.setFont("Arial", 12)
        lines = re.split(r'[\r\n]+', languages)
        for line in lines:
            p.drawString(50, y, "• " + line)
            y -= 15
        y = y - 20

        p.showPage()
        p.save()

        return response