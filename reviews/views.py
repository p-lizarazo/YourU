from django.shortcuts import render, redirect
from .models import *
from django.core import serializers

# Create your views here.


def index(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        context = {'reviews': reviews}
        return render(request, 'reviews/index.html', context)


def detail_review(request, rev_id):
    if request.method == 'GET':
        review = Review.objects.get(id=rev_id)
        context = {'review': review}
        return render(request, 'reviews/detail_rev.html', context)
    pass


def create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            universtities = University.objects.all()

            programs = serializers.serialize('json', Program.objects.all())
            faculties = serializers.serialize('json', Faculty.objects.all())

            context = {'programs': programs, 'universities': universtities, 'faculties': faculties}
            return render(request, 'reviews/create_review.html', context)
        elif request.method == 'POST':
            program = Program.objects.get(id=request.POST.get('program'))
            program_desc = request.POST.get('descProgram')
            uni_desc = request.POST.get('descUni')
            uni_cal = request.POST.get('uni_cal')
            prog_cal = request.POST.get('prog_cal')

            new_review = Review( university= program.faculty.university , program= program, user= request.user,
                                uni_description= uni_desc, prog_description= program_desc,
                                 uni_calification= uni_cal, prog_calification= prog_cal,
                                 )
            new_review.save()

            return redirect('reviews')
    else:
        return redirect('/accounts/login/')
