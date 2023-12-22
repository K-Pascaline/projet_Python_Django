# Dans le fichier admin.py de votre application
from django.contrib import admin
from .models import Etudiant, Matiere, Notation

admin.site.register(Etudiant)
admin.site.register(Matiere)
admin.site.register(Notation)
