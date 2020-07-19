from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_plan, name='programs'),
    path('create/', views.create_plan ),
    path('<int:plan_id>/', views.detail_plan, name='detail_plan'),
]