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


class Produto(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    tipo = models.CharField(max_length=80)
    peso = models.FloatField()
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    login = models.CharField(max_length=120)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Despensa(models.Model):
    nome = models.CharField(max_length=80)
    localizacao = models.CharField(max_length=120)

    def __str__(self):
        return self.nome


class ProdutoDespensa(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    despensa = models.ForeignKey(Despensa, on_delete=models.CASCADE)
    validade = models.DateField()
    quantidade = models.IntegerField()

    def __str__(self):
        return self.quantidade


class Receita(models.Model):
    titulo = models.CharField(max_length=80)
    modoPreparo = models.TextField()
    tempoExecucao = models.TimeField()
    quantidade = models.IntegerField()
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo


class ProdutoReceita(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.quantidade


class Favorita(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.receita + ' ' + self.cliente
