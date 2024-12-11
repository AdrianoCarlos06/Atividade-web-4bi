from django.db import models

class Especie(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
