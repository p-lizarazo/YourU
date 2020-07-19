from django.db import models
from django.conf import settings
from geolocalization.models import *
from django_google_maps import fields as map_fields
from django.utils import timezone
# Create your models here.


class University(models.Model):
    PAIS = (
        ('Colombia', 'Colombia'), ('Ecuador', 'Ecuador'), ('Mexico', 'Mexico'),
        ('Rusia', 'Rusia'), ('Inglaterra', 'Inglaterra'), ( 'Perú', 'Perú'),
        ('Estados Unidos', 'Estados Unidos'), ('Chile', 'Chile')

    )

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    rating = models.FloatField(default=0.0)
    logo = models.ImageField(upload_to='images/', blank=True)
    times_higher_ed = models.CharField(max_length=30,default='No aplica')
    web_link = models.URLField(blank=True)
    address = map_fields.AddressField(max_length=200, blank=True)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True)
    pais = models.CharField(max_length=15, choices=PAIS, blank=True)
    ciudad = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ',' + self.university.name


class Scholarship(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Program(models.Model):
    TIPO = (
        ('preg','pregrado'),
        ('pos', 'posgrado')
    )

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    tuition_fee = models.DecimalField(max_digits=20, decimal_places=0)
    scholarships = models.ManyToManyField(Scholarship, blank=True)
    prog_calification = models.FloatField(default=0.0)
    study_program = models.FileField(upload_to='documents/', blank=True)
    tipo = models.CharField(max_length=11, choices=TIPO, blank=True)

    def __str__(self):
        return self.name + ',' + self.faculty.university.name


class Period(models.Model):
    name = models.CharField(max_length=200)
    application_deadline = models.DateField(default=timezone.now)
    application_startline = models.DateField(default=timezone.now)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.program.__str__() + self.name
