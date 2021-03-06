# Generated by Django 2.0.13 on 2019-05-23 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0010_university_ciudad'),
        ('my_plan', '0006_auto_20190523_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myplan',
            name='period',
        ),
        migrations.AddField(
            model_name='myplan',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='university.Program'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myplan',
            name='cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_plan.CostoDeVida'),
        ),
    ]
