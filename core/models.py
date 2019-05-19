from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=80)

    def __str__(self):
        return self.nome


class Medida(models.Model):
    nome = models.CharField(max_length=80)
    valor = models.FloatField()

    def __str__(self):
        return self.nome
