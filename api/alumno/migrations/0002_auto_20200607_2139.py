# Generated by Django 2.1.14 on 2020-06-08 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='alumno',
            table='alumno_alumno',
        ),
        migrations.AlterModelTable(
            name='carrera',
            table='alumno_carrera',
        ),
    ]
