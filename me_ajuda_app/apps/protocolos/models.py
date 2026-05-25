from django.db import models

# Create your models here.
class Protocolo(models.Model):
    protocolo_numero = models.CharField('Número do Protocolo', max_length=20)
    gerado_em = models.DateTimeField('Gerado em', auto_now_add=True)
    prazo = models.DateField('Prazo')
    ocorrencia = models.OneToOneField('ocorrencias.Ocorrencia', on_delete=models.CASCADE)