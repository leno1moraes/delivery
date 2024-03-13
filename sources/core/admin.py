from django.contrib import admin

from .models import Unidade, Produto

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'preco', 'unidade']

admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Produto, ProdutoAdmin)
