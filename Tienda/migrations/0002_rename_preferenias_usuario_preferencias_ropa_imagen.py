# Generated by Django 4.2.7 on 2023-11-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='preferenias',
            new_name='preferencias',
        ),
        migrations.AddField(
            model_name='ropa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='ropa/'),
        ),
    ]