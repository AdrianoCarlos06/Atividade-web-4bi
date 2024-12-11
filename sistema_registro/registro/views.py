from django.shortcuts import render, get_object_or_404, redirect
from .models import Especie, Animal


def index(request):
    return render(request, 'registro/index.html')

def lista_especies(request):
    especies = Especie.objects.all()
    return render(request, 'registro/lista_especies.html', {'especies': especies})

def nova_especie(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Especie.objects.create(nome=nome)
        return redirect('lista_especies')
    return render(request, 'registro/form_especie.html')

def editar_especie(request, id):
    especie = get_object_or_404(Especie, id=id)
    if request.method == 'POST':
        especie.nome = request.POST.get('nome')
        especie.save()
        return redirect('lista_especies')
    return render(request, 'registro/form_especie.html', {'especie': especie})

def excluir_especie(request, id):
    especie = get_object_or_404(Especie, id=id)
    especie.delete()
    return redirect('lista_especies')

def detalhe_especie(request, id):
    especie = get_object_or_404(Especie, id=id)
    return render(request, 'registro/detail_especie.html', {'especie': especie})

def confirmar_exclusao_especie(request, id):
    especie = get_object_or_404(Especie, id=id)
    if request.method == 'POST':
        especie.delete()
        return redirect('lista_especies')
    return render(request, 'registro/confirm_delete_especie.html', {'especie': especie})

def lista_animais(request):
    animais = Animal.objects.all()
    return render(request, 'registro/lista_animais.html', {'animais': animais})

def novo_animal(request):
    especies = Especie.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        especie_id = request.POST.get('especie')
        especie = get_object_or_404(Especie, id=especie_id)
        Animal.objects.create(nome=nome, idade=idade, especie=especie)
        return redirect('lista_animais')
    return render(request, 'registro/form_animal.html', {'especies': especies})

def editar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    especies = Especie.objects.all()
    if request.method == 'POST':
        animal.nome = request.POST.get('nome')
        animal.idade = request.POST.get('idade')
        especie_id = request.POST.get('especie')
        animal.especie = get_object_or_404(Especie, id=especie_id)
        animal.save()
        return redirect('lista_animais')
    return render(request, 'registro/form_animal.html', {'animal': animal, 'especies': especies})

def detalhe_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    return render(request, 'registro/detail_animal.html', {'animal': animal})

def confirmar_exclusao_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal.delete()
        return redirect('lista_animais')
    return render(request, 'registro/confirm_delete_animal.html', {'animal': animal})
