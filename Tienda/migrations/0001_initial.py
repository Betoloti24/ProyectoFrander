# Generated by Django 4.2.7 on 2023-11-25 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('País', 'País'), ('Ciudad', 'Ciudad')], max_length=10)),
                ('id_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tienda.ubicacion')),
            ],
            options={
                'verbose_name': 'Ubicación',
                'verbose_name_plural': 'Ubicaciones',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cedula', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('f_nacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=30)),
                ('id_pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tienda.ubicacion')),
                ('preferenias', models.ManyToManyField(to='Tienda.categoria')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Ropa',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=9)),
                ('marca', models.CharField(max_length=20)),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('tipo', models.CharField(choices=[('Camisa', 'Camisa'), ('Pantalón', 'Pantalón'), ('Zapatos', 'Zapatos'), ('Interior', 'Interior')], max_length=20)),
                ('categorias', models.ManyToManyField(to='Tienda.categoria')),
            ],
            options={
                'verbose_name': 'Ropa',
                'verbose_name_plural': 'Ropas',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('f_facturacion', models.DateField()),
                ('monto_total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.usuario')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('id_factura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tienda.factura')),
                ('id_ropa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.ropa')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.usuario')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carritos',
            },
        ),
    ]
