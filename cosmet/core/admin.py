from django.contrib import admin
from cosmet.core.models import fornecedor, produto, funcionario, clientes, venda, produto_Venda, cargo


class fornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_filter = ('nome', )

admin.site.register(fornecedor, fornecedorAdmin)

class produtoAdmin(admin.ModelAdmin):
    list_display = ('id', 'preco', 'codBarra', 'marca', 'descricao', 'fornecedor')
    list_filter = ('id', 'descricao')

admin.site.register(produto, produtoAdmin)

class cargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'salario', 'horario_entrada', 'horario_saida')
    list_filter = ('id', 'nome')

admin.site.register(cargo, cargoAdmin)


class funcionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'idade', 'cargo')
    list_filter = ('id', 'nome', 'cpf')

admin.site.register(funcionario, funcionarioAdmin)

class clientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpf', 'nome', 'endereco', 'estado', 'cidade', 'telefone', 'dataCadastro')
    list_filter = ('id', 'cpf', 'nome')

admin.site.register(clientes, clientesAdmin)

class vendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_venda', 'data')
    list_filter = ('id', 'numero_venda')

admin.site.register(venda, vendaAdmin)

class produto_VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'quantidade', 'venda', 'valor')
    list_filter = ('id', 'venda')

admin.site.register(produto_Venda, produto_VendaAdmin)