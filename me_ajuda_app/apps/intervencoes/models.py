from django.db import models

# Create your models here.
class Intervencao(models.Model):
    titulo = models.CharField('Título', max_length=50)
    data_exec = models.DateField('Data de Execução')
    relato = models.TextField('Relato')
    custo_trab = models.DecimalField('Custo do Trabalho', max_digits=10, decimal_places=2)
    doc = models.FileField('Documento', upload_to='intervencoes/', null=True, blank=True)
    ocorrencia = models.ForeignKey('ocorrencias.Ocorrencia', on_delete=models.CASCADE, related_name='intervencoes')
    funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.CASCADE, related_name='intervencoes')
