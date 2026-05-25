from django.db import models

from secretarias.models import Secretaria


# Create your models here.
class Servico(models.Model):
    nome = models.CharField("Nome", max_length=50)
    descricao = models.CharField("Descricao", max_length=200)
    nivel_prioridade = models.IntegerField("Nivel de Prioridade")
    secretaria = models.ForeignKey(
        Secretaria, on_delete=models.CASCADE, related_name="servicos"
    )

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ["id"]

    def __str__(self):
        return f"{self.nome}"
