from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<cidade_nome>/', views.delete_cidade, name='deletar_cidade')
]
