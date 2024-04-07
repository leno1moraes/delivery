from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

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
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(unique=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido {self.id}" 
    
    def calcular_total(self):
        total_pedido = sum(produto.preco for produto in self.produto.all())
        self.total = total_pedido
        self.save() 

    def save(self, *args, **kwargs):
        self.calcular_total()  
        super().save(*args, **kwargs)   