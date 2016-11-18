from django.db import models
from django.db.models import Sum

class fornecedor(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome

class produto(models.Model):
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    codBarra = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    fornecedor = models.ForeignKey('fornecedor')


    class Meta:
        ordering = ['descricao']
        verbose_name = 'produto'


    def __str__(self):
        return self.descricao

class cargo(models.Model):
    nome = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=5, decimal_places=2, default=800)
    horario_entrada = models.IntegerField()
    horario_saida = models.IntegerField()

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    idade = models.IntegerField()
    cargo = models.ForeignKey('cargo')

    class Meta:
        ordering = ['nome']
        verbose_name = 'funcionario'


    def __str__(self):
        return self.nome

class clientes(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.IntegerField()
    endereco = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.IntegerField()
    dataCadastro = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'

    def __str__(self):
        return self.nome

class venda(models.Model):
    numero_venda = models.CharField(max_length=20)
    data = models.DateField(auto_now_add=True)
    cliente = models.ManyToManyField('clientes')
    vendedor = models.ManyToManyField('funcionario')

    class Meta:
        ordering = ['numero_venda']
        verbose_name = 'Venda'

    def __str__(self):
        return self.numero_venda

class produto_Venda(models.Model):

    produto = models.ForeignKey('produto')
    quantidade = models.IntegerField()
    venda = models.ForeignKey('venda')
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ['produto']
        verbose_name = 'Produto Venda'
