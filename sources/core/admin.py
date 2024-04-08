from django.contrib import admin

from .models import Unidade, Produto, Pedido

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao']

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'preco', 'unidade', 'fornecedor']

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'cliente', 'produtos', 'quantidade', 'total', 'status']

admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido, PedidoAdmin)

