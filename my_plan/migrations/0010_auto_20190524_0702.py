# Generated by Django 2.0.13 on 2019-05-24 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_plan', '0009_auto_20190524_0429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myplan',
            name='email_notify',
        ),
        migrations.AddField(
            model_name='myplan',
            name='application_deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myplan',
            name='costo_comida',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myplan',
            name='costo_habitacion',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myplan',
            name='costo_matricula',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myplan',
            name='costo_transporte',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='myplan',
            name='cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_plan.CostoDeVida'),
        ),
    ]
