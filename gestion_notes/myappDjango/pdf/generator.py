from reportlab.pdfgen import canvas

def generate_student_report(student_name, grades):
    pdf_filename = f"{student_name}_report.pdf"
    c = canvas.Canvas(pdf_filename)
    c.drawString(100, 800, f"Student: {student_name}")

    # Ajoutez le reste du contenu du rapport en utilisant les données des notes
    c.drawString(100, 780, "Grades:")
    y_position = 760
    for grade in grades:
        c.drawString(120, y_position, f"- {grade}")
        y_position -= 20

    # Calcul de la moyenne annuelle (à adapter selon vos besoins)
    average_grade = sum(grades) / len(grades)
    c.drawString(100, y_position, f"Average Grade: {average_grade:.2f}")

    c.save()

# Exemple d'utilisation
student_name = "kihe Pasca"
grades = [90, 85, 92, 88]
generate_student_report(student_name, grades)
