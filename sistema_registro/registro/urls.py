from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('especies/', views.lista_especies, name='lista_especies'),
    path('especies/nova/', views.nova_especie, name='nova_especie'),
    path('especies/<int:id>/editar/', views.editar_especie, name='editar_especie'),
    path('especies/<int:id>/excluir/', views.confirmar_exclusao_especie, name='confirmar_exclusao_especie'),
    path('especies/<int:id>/', views.detalhe_especie, name='detalhe_especie'),
    path('animais/', views.lista_animais, name='lista_animais'),
    path('animais/novo/', views.novo_animal, name='novo_animal'),
    path('animais/<int:id>/editar/', views.editar_animal, name='editar_animal'),
    path('animais/<int:id>/excluir/', views.confirmar_exclusao_animal, name='confirmar_exclusao_animal'),
    path('animais/<int:id>/', views.detalhe_animal, name='detalhe_animal'),
]
