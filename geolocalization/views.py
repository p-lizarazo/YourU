from django.shortcuts import render
from university.models import University

# Create your views here.
def index(request):
    if request.method == 'GET':
        context = {'universities' : University.objects.all()}
        return render(request, 'geolocalization/index.html', context)