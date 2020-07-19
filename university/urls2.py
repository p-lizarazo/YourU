from django.urls import path

from . import views

urlpatterns = [
    path('', views.programs_list, name='programs'),
]