from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='reviews'),
    path('create/', views.create, name='create_review'),
    path('<int:rev_id>/', views.detail_review, name='detail_review'),
]