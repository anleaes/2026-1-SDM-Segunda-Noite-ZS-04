from django.db import models

# Create your models here.
class IntervencaoEquipamento(models.Model):
    horas_usado = models.IntegerField('Horas Usado')
    custo_total = models.FloatField('Custo Total')
    intervencao = models.ForeignKey('intervencoes.Intervencao', on_delete=models.CASCADE)
    equipamento = models.ForeignKey('equipamentos.Equipamento', on_delete=models.CASCADE)