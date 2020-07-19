from django.urls import path

from . import views

urlpatterns = [
    path('', views.university, name='university'),
    path('<int:u_id>/', views.faculty, name='faculty'),
    path('<int:u_id>/<int:faculty_id>/', views.program, name='program'),
    path('<int:u_id>/<int:faculty_id>/<int:program_id>/', views.detailprog, name='detail_prog'),
]