# Generated by Django 4.2.7 on 2023-11-10 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Local", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="compra",
            name="cantidad",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)]
            ),
        ),
        migrations.AlterField(
            model_name="juego",
            name="precio_compra",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=8,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
