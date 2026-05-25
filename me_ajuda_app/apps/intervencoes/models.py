from django.db import models

from funcionarios.models import Funcionario
from ocorrencias.models import Ocorrencia


# Create your models here.
class Intervencao(models.Model):
    titulo = models.CharField("Título", max_length=50)
    data_exec = models.DateField("Data de Execução")
    relato = models.TextField("Relato")
    custo_trab = models.DecimalField(
        "Custo do Trabalho", max_digits=10, decimal_places=2
    )
    doc = models.FileField(
        "Documento", upload_to="intervencoes/", null=True, blank=True
    )
    ocorrencia = models.ForeignKey(Ocorrencia, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Intervenção"
        verbose_name_plural = "Intervenções"
        ordering = ["id"]

    def __str__(self):
        return f"{self.titulo} - {self.data_exec}"
