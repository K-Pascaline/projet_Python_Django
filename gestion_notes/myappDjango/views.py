from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Avg
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Notation, Etudiant


def student_notes(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    all_notes = Notation.objects.filter(etudiant=student)

    context = {
        'student': student,
        'all_notes': all_notes,
    }

    # Generate PDF
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer)

    # Add student information
    pdf.drawString(100, 800, f"Student: {student.nom_etudiant} {student.prenom_etudiant}")

    # Add notes
    y_position = 780
    for note in all_notes:
        pdf.drawString(100, y_position, f"{note.matiere.nom_matiere}: {note.note}")
        y_position -= 20

    pdf.showPage()
    pdf.save()

    # Get PDF content from buffer
    pdf_buffer.seek(0)
    response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'filename={student.nom_etudiant}_{student.prenom_etudiant}_notes.pdf'
    pdf_buffer.close()
    
    return response

def student_average(request, student_id):
    student = Etudiant.objects.get(pk=student_id)
    all_notes = Notation.objects.filter(etudiant=student)
    average = all_notes.aggregate(avg=Avg('note'))['avg']

    context = {
        'student': student,
        'all_notes': all_notes,
        'average': average,
    }
    

def student_report(request, student_id):
    student = get_object_or_404(Etudiant, pk=student_id)
    pdf_buffer = student.generate_pdf_report()

    # Get PDF content from buffer
    pdf_buffer.seek(0)
    response = HttpResponse(pdf_buffer.read(), content_type='application/pdf')
    response['Content-Disposition'] = f'filename={student.nom_etudiant}_{student.prenom_etudiant}_report.pdf'
    pdf_buffer.close()

    return response

