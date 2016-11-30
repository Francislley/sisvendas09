from django.db import models
from django.db.models import Sum

class fornecedor(models.Model):

    nome = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=16, blank=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome

class produto(models.Model):

    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2, default=0)
    codBarra = models.CharField('Código de Barras', max_length=50)
    marca = models.CharField('Marca', max_length=50)
    descricao = models.CharField('Descrição', max_length=100)
    fornecedor = models.ForeignKey('fornecedor')
    estoque_entrada = models.IntegerField('Estoque de entrada', null=False)

    class Meta:
        ordering = ['descricao']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'


    def __str__(self):
        return self.descricao

    def estoque(self):

        entradas = produto.objects.filter(pk=self.pk).aggregate(Sum('estoque_entrada'))
        vendas = produto_Venda.objects.filter(produto=self).aggregate(Sum('quantidade'))


        if entradas.get('estoque_entrada__sum') == 0:
            return 'Estoque Não Cadastrado'
        elif vendas.get('quantidade__sum') == None:
            return entradas.get('estoque_entrada__sum')
        else:
            return entradas.get('estoque_entrada__sum') - vendas.get('quantidade__sum')


class cargo(models.Model):

    nome = models.CharField('Nome', max_length=200)
    salario = models.DecimalField('Salário', max_digits=5, decimal_places=2, default=800)
    horario_entrada = models.TimeField('Horário de Entrada')
    horario_saida = models.TimeField('Horário de Saída')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class funcionario(models.Model):

    nome = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=11)
    idade = models.IntegerField('Idade')
    cargo = models.ForeignKey('cargo')

    class Meta:
        ordering = ['nome']
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'


    def __str__(self):
        return self.nome

class clientes(models.Model):

    nome = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=11)
    endereco = models.CharField('Endereço', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    dataCadastro = models.DateField('Data Cadastro', auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return self.nome


class venda(models.Model):

    numero_venda = models.IntegerField('Número da Venda')
    data = models.DateField('Data da Venda', auto_now_add=True)
    cliente = models.ForeignKey('clientes', verbose_name='Cliente')
    vendedor = models.ForeignKey('funcionario', verbose_name='Vendedor')


    class Meta:
        ordering = ['numero_venda']
        verbose_name = 'Venda'


    def __str__(self):
        return str(self.numero_venda)


class produto_Venda(models.Model):

    produto = models.ForeignKey('produto', verbose_name='Produto')
    quantidade = models.IntegerField('Quantidade', null=False)
    venda = models.ForeignKey('venda', verbose_name='Número da Venda')


    class Meta:
        ordering = ['produto']
        verbose_name = 'Produto Venda'
        verbose_name_plural = 'Produtos Venda'

