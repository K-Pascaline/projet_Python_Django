# Generated by Django 5.0 on 2023-12-21 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_etudiant', models.CharField(max_length=255)),
                ('prenom_etudiant', models.CharField(max_length=255)),
                ('numero_etudiant', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_matiere', models.CharField(max_length=255)),
                ('code_matiere', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Notation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_notation', models.DateField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappDjango.etudiant')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myappDjango.matiere')),
            ],
        ),
    ]