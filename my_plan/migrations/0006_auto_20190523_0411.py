# Generated by Django 2.0.13 on 2019-05-23 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_plan', '0005_auto_20190523_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myplan',
            name='cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_plan.CostoDeVida'),
        ),
    ]
