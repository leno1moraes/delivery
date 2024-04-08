from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


STATUS_CHOICES = (
        ("1", "Aberto"),
        ("2", "Atendimento"),
        ("3", "Concluído")
    )

class Unidade(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.descricao

class Produto(models.Model):
    descricao = models.CharField('Descrição', max_length=100) 
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.descricao


class Pedido(models.Model):
    data = models.DateTimeField(unique=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    quantidade = models.BigIntegerField(default=0)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=False)

    def __str__(self):
        return f"Pedido {self.id}"