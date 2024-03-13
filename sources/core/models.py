from django.db import models


class Unidade(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.descricao

class Produto(models.Model):
    descricao = models.CharField('Descrição', max_length=100) 
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
