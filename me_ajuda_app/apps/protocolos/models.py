from django.db import models

from ocorrencias.models import Ocorrencia


# Create your models here.
class Protocolo(models.Model):
    protocolo_numero = models.CharField("Número do Protocolo", max_length=20)
    gerado_em = models.DateTimeField("Gerado em", auto_now_add=True)
    prazo = models.DateField("Prazo")
    ocorrencia = models.OneToOneField(Ocorrencia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Protocolo"
        verbose_name_plural = "Protocolos"
        ordering = ["id"]

    def __str__(self):
        return f"{self.protocolo_numero}"
