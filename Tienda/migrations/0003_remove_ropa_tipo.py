# Generated by Django 4.2.7 on 2023-11-28 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0002_rename_preferenias_usuario_preferencias_ropa_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ropa',
            name='tipo',
        ),
    ]
