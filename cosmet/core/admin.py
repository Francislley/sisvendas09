from django.contrib import admin
from cosmet.core.models import fornecedor, produto, funcionario, \
    clientes, venda, produto_Venda, cargo


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

# Esta classe exibe os produtos quando vc entra em venda no admin
class ProdutoVendaAdminInline(admin.TabularInline):

    model = produto_Venda
    extra = 0


class vendaAdmin(admin.ModelAdmin):

    inlines = [ProdutoVendaAdminInline]
    list_display = ('id', 'numero_venda', 'data', 'cliente', 'vendedor', 'valor_total_venda')
    list_filter = ('id', 'numero_venda')


    def valor_total_venda(self,obj):

        soma = 0
        produtos = produto_Venda.objects.filter(venda__id=obj.pk)

        for item in produtos:
            soma += (item.produto.preco * item.quantidade)

        return soma


    valor_total_venda.short_description = 'Valor Total'


admin.site.register(venda, vendaAdmin)



class produto_VendaAdmin(admin.ModelAdmin):

    list_display = ('id', 'produto', 'quantidade', 'venda', 'subtotal')
    list_filter = ('id', 'venda')


    def subtotal(self, obj):

        subtotal = obj.produto.preco * obj.quantidade
        return subtotal

    subtotal.short_description = 'Subtotal'


admin.site.register(produto_Venda, produto_VendaAdmin)