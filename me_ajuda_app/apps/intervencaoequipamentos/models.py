from django.db import models
from django.core.validators import MinValueValidator
from intervencoes.models import Intervencao
from equipamentos.models import Equipamento


# Create your models here.
class IntervencaoEquipamento(models.Model):
    horas_usado = models.IntegerField("Horas Usado")
    custo_total = models.FloatField("Custo Total", validators=[MinValueValidator(0.0)])
    intervencao = models.ForeignKey(Intervencao, on_delete=models.CASCADE, related_name='equipamentos')
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='intervencoes')

    class Meta:
        verbose_name = "Equipamento da Intervenção"
        verbose_name_plural = "Equipamentos das Intervenções"
        ordering = ["id"]

    def __str__(self):
        return f"{self.intervencao} - {self.equipamento} - {self.horas_usado}h - R${self.custo_total}"
