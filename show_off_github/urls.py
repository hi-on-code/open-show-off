from django.urls import path

from . import views

urlpatterns = [
    path('userName/', views.get_user_name, name='get_user_name'),
    path('', views.index, name='index'),
    path('<str:userName>', views.index, name='index'),
]
