# Generated by Django 4.0.4 on 2022-06-04 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'ordering': ['UserAcces', 'Nombre', 'ApellidoPaterno', 'ApellidoMaterno', 'Correo', 'Telefono', 'Pass', 'Pass', 'Roll'], 'verbose_name': 'Usuarios', 'verbose_name_plural': 'Usuarioss'},
        ),
        migrations.AlterUniqueTogether(
            name='usuarios',
            unique_together={('UserAcces',)},
        ),
        migrations.AlterModelTable(
            name='usuarios',
            table='Usuarios',
        ),
    ]
