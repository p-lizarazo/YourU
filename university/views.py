from django.shortcuts import render, HttpResponse, Http404, redirect
from .models import *
from django.utils import timezone
import datetime
# Create your views here.
def university(request):
    if request.method == 'GET':
        order = request.GET.get('order_by', 'AZ')
        order_map = { 'AZ': 'name' , 'ZA' : '-name' , 'rating': '-rating'}

        country = request.GET.get('country', "")
        lower_rating = request.GET.get('low_range', '0')
        higher_rating = request.GET.get('high_range', '5')
        uname = request.GET.get('uname', "")


        universities = University.objects.all().order_by(order_map[order] )

        if uname != "":
            universities = universities.filter(name__icontains=uname)

        if country != "":
            universities = universities.filter(pais__icontains=country)


        if lower_rating != '0':
            universities = universities.filter(rating__gte=float(lower_rating) )

        if higher_rating != '5':
            universities = universities.filter( rating__lte=float(higher_rating) )

        context = {'universities': universities}
        return render(request, 'university/universities.html', context)
    else:
        return Http404('Not Allowed')


def faculty(request, u_id): #El id de la universidad
    if request.method == 'GET':
        my_u = University.objects.get(id=u_id)
        faculties = Faculty.objects.filter(university=u_id)
        context = {'my_u': my_u ,'faculties': faculties, 'u_id': u_id}
        return render(request, 'university/faculties.html', context)
    else:
        return Http404('Not Allowed')


def program(request, u_id, faculty_id): #Necesito id de la facultad
    if request.method == 'GET':
        my_u = University.objects.get(id=u_id)
        programs = Program.objects.filter(faculty=faculty_id)
        my_faculty = Faculty.objects.get(id=faculty_id)
        context = {'programs' : programs,'u_id': u_id, 'faculty_id':faculty_id, 'my_fac': my_faculty, 'my_u' : my_u }
        return render(request, 'university/programs.html', context)
    else:
        return Http404('Not Allowed')


def detailprog(request, u_id, faculty_id, program_id):
    if request.method == 'GET':
        my_u = University.objects.get(id=u_id)
        my_faculty = Faculty.objects.get(id=faculty_id)
        my_program = Program.objects.get(id=program_id)
        periods = Period.objects.filter(program=my_program)
        scholarships = [val for val in Scholarship.objects.all() if val in my_program.scholarships.all() ]

        context = {'my_program': my_program, 'u_id': u_id, 'faculty_id': faculty_id, 'my_fac': my_faculty, 'my_u': my_u,
                   'periods': periods, 'scholarships': scholarships }
        return render(request, 'university/detailprog.html',context)
    else:
        return Http404('Not Allowed')


def programs_list(request):
    if request.method == 'GET':
        order = request.GET.get('order_by', 'AZ')
        order_map = {'AZ': 'name', 'ZA': '-name', 'rating': '-prog_calification'}

        pregrado = request.GET.get('pregrado', 'None')
        posgrado = request.GET.get('posgrado', 'None')
        inscripcion = request.GET.get('insc', 'None')
        lower_rating = request.GET.get('low_range', '0')
        higher_rating = request.GET.get('high_range', '5')
        progname = request.GET.get('progname',"")

        programs = Program.objects.all().order_by(order_map[order])

        if pregrado == "true" and posgrado != "true":
            programs = programs.filter(tipo='preg')
        if posgrado == "true" and pregrado !="true":
            programs = programs.filter(tipo='pos')
        if inscripcion == "true":
            current_time = datetime.datetime.now()
            periods = Period.objects.all()

            periods = periods.filter(application_startline__lte=current_time)
            periods = periods.filter(application_deadline__gte=current_time)
            ids = [x.program_id for x in periods]
            programs = programs.filter(id__in=ids)

        if lower_rating != '0':
            programs = programs.filter(prog_calification__gte=float(lower_rating))

        if higher_rating != '5':
            programs = programs.filter(prog_calification__lte=float(higher_rating))

        if progname != "":
            programs = programs.filter(name__icontains=progname)

        context = {'programs': programs}

        return render(request, 'university/list_programs.html', context)
    else:
        return Http404('Not Allowed')
