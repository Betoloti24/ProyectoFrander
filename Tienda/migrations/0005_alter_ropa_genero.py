# Generated by Django 4.2.7 on 2023-12-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0004_usuario_clave_acceso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropa',
            name='genero',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Unisex', 'Unisex')], max_length=10),
        ),
    ]
