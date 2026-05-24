from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descricao', max_length=200)
    nivel_prioridade = models.IntegerField('Nivel de Prioridade')
    secretaria = models.ForeignKey('secretarias.Secretaria', on_delete=models.CASCADE, related_name='servicos')