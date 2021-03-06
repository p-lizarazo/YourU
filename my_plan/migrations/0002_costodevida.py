# Generated by Django 2.0.13 on 2019-05-23 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='costoDeVida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(choices=[('Colombia', 'Colombia'), ('Ecuador', 'Ecuador'), ('Mexico', 'Mexico'), ('Rusia', 'Rusia'), ('Inglaterra', 'Inglaterra'), ('Perú', 'Perú'), ('Estados Unidos', 'Estados Unidos'), ('Chile', 'Chile'), ('Ecuador', 'Ecuador')], max_length=15, unique=True)),
                ('ciudad', models.CharField(blank=True, max_length=15)),
                ('costo_habitacion', models.DecimalField(decimal_places=0, max_digits=20)),
                ('costo_comida', models.DecimalField(decimal_places=0, max_digits=20)),
                ('costo_transporte', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
        ),
    ]
