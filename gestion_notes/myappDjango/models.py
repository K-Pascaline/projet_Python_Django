from django.db import models
from django.db.models import Avg
from reportlab.pdfgen import canvas
from io import BytesIO

class Matiere(models.Model):
    nom_matiere = models.CharField(max_length=255)
    code_matiere = models.CharField(max_length=10)

    def __str__(self):
        return self.nom_matiere

class Etudiant(models.Model):
    nom_etudiant = models.CharField(max_length=255)
    prenom_etudiant = models.CharField(max_length=255)
    numero_etudiant = models.CharField(max_length=20, unique=True)


    def calculate_average_grade(self):
        total_grade = 0
        total_notations = 0
        for notation in self.notation_set.all():
            total_grade += notation.note
            total_notations += 1
        return total_grade / total_notations if total_notations > 0 else 0

    def __str__(self):
        return f"{self.nom_etudiant} {self.prenom_etudiant} - (id): {self.id}"
    
    def generate_pdf_report(self):
        all_notes = Notation.objects.filter(etudiant=self)

        pdf_buffer = BytesIO()
        pdf = canvas.Canvas(pdf_buffer)

        # Add student information
        pdf.drawString(100, 800, f"Student: {self.nom_etudiant} {self.prenom_etudiant}")

        # Add notes
        y_position = 780
        for note in all_notes:
            pdf.drawString(100, y_position, f"{note.matiere.nom_matiere}: {note.note}")
            y_position -= 20

        # Add average
        average = all_notes.aggregate(avg=Avg('note'))['avg']
        pdf.drawString(100, y_position - 20, f"Average: {average}")

        pdf.showPage()
        pdf.save()

        # Get PDF content from buffer
        pdf_buffer.seek(0)
        return pdf_buffer

class Notation(models.Model):
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)
    date_notation = models.DateField()

    def __str__(self):
        return f"{self.etudiant} - {self.matiere} - {self.note}"
