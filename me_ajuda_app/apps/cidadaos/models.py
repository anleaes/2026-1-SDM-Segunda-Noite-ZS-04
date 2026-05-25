from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Cidadao(Usuario):
    fone = models.CharField('Fone', max_length=20)
    endereco = models.CharField('Endereco', max_length=200)
    cep = models.CharField('CEP', max_length=10)
    bairro = models.CharField('Bairro', max_length=100)

    class Meta:
        verbose_name = 'Cidadão'
        verbose_name_plural = 'Cidadãos'
        ordering =['id']

    def __str__(self):
        return  super().__str__()