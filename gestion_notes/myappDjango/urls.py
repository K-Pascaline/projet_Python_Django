# myappDjango/urls.py

#from django.urls import path
#from .views import notation_list, NotationPDFView

#app_name = 'myappDjango'

#urlpatterns = [
 #   path('notations/', notation_list, name='notation_list'),
  #  path('generate_pdf/<int:etudiant_id>/', NotationPDFView.as_view(), name='generate_pdf'),
#]

# urls.py
from django.urls import path
from .views import student_notes, student_average, student_report

app_name = 'myappDjango'

urlpatterns = [
    path('student/<int:student_id>/notes/', student_notes, name='student_notes'),
    path('student/<int:student_id>/average/', student_average, name='student_average'),
    path('student/<int:student_id>/report/', student_report, name='student_report'),
]




