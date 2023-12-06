# Generated by Django 4.2.7 on 2023-12-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Tienda", "0007_alter_factura_f_facturacion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="correo",
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="preferencias",
            field=models.ManyToManyField(blank=True, to="Tienda.categoria"),
        ),
    ]