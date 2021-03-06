# Generated by Django 4.0.4 on 2022-05-28 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('IdProyect', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ProyectName', models.CharField(max_length=80)),
                ('UserAccesArq', models.CharField(max_length=20)),
                ('UserAccesAdm', models.CharField(max_length=20)),
                ('Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('UserAcces', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
                ('ApellidoPaterno', models.CharField(max_length=20)),
                ('ApellidoMaterno', models.CharField(max_length=20)),
                ('Correo', models.EmailField(max_length=70)),
                ('Telefono', models.IntegerField(max_length=10)),
                ('Pass', models.CharField(max_length=80)),
                ('Roll', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('IdKey', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('IdMaterial', models.CharField(max_length=20)),
                ('MaterialName', models.CharField(max_length=80)),
                ('MaterialDeseado', models.IntegerField(max_length=10)),
                ('MaterialEntregado', models.IntegerField(max_length=10)),
                ('UndiadMaterial', models.CharField(max_length=20)),
                ('FechaEntrega', models.DateField()),
                ('IdProyect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proyectos')),
            ],
        ),
    ]
