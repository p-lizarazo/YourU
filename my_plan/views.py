from django.shortcuts import render, redirect

from university.models import *
from .models import *
from django.core import serializers
import datetime

# Create your views here.
def my_plan(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            username = request.user.username
            my_plans = MyPlan.objects.filter(user__username=username)
            context = {'my_plans': my_plans}
            return render(request, 'my_plan/my_plan.html', context)
    else:
        return redirect('/accounts/login/')

def create_plan(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            universtities = University.objects.all()

            programs = serializers.serialize('json', Program.objects.all())
            faculties = serializers.serialize('json', Faculty.objects.all())

            context = {'programs': programs, 'universities': universtities, 'faculties': faculties}
            return render(request, 'my_plan/create.html', context)
        elif request.method == 'POST':
            plan_name = request.POST.get('plan_name')
            program = Program.objects.get(id=request.POST.get('program'))
            costo_matricula = request.POST.get('costo_matricula')
            costo_habitacion = request.POST.get('costo_habitacion')
            costo_alimentacion = request.POST.get('costo_alimentacion')
            costo_transporte = request.POST.get('costo_transporte')

            costo_vida = CostoDeVida.objects.get(pais=program.faculty.university.pais, ciudad= program.faculty.university.ciudad)

            if(costo_matricula == "True"):
                costo_matricula=True
            else:
                costo_matricula=False

            if (costo_habitacion == "True"):
                costo_habitacion = True
            else:
                costo_habitacion = False

            if (costo_alimentacion == "True"):
                costo_alimentacion = True
            else:
                costo_alimentacion = False

            if (costo_transporte == "True"):
                costo_transporte = True
            else:
                costo_transporte = False

            new_plan = MyPlan(name=plan_name, program=program, cost=costo_vida, user=request.user,
                           costo_matricula=costo_matricula, costo_habitacion=costo_habitacion, costo_comida=costo_alimentacion,
                           costo_transporte=costo_transporte)
            new_plan.save()
            return redirect('/accounts/login/')
        else:
            pass
    else:
        return redirect('programs')


def detail_plan(request, plan_id):
    if request.method == 'GET':
        my_plan = MyPlan.objects.get(id=plan_id)

        total = 0
        if my_plan.costo_transporte == True:
            total+=my_plan.cost.costo_transporte
        if my_plan.costo_habitacion == True:
            total+=my_plan.cost.costo_habitacion
        if my_plan.costo_comida == True:
            total+=my_plan.cost.costo_comida

        context = {'my_plan': my_plan, 'total':total}
        return render(request, 'my_plan/detail_plan.html', context)
    pass