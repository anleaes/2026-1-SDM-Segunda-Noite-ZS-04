from django.db import models

from cidadaos.models import Cidadao
from servicos.models import Servico


# Create your models here.
class Ocorrencia(models.Model):
    titulo = models.CharField("Titulo", max_length=100)
    descricao = models.TextField("Descrição")
    endereco = models.CharField("Endereço", max_length=255)
    numero = models.CharField("Número", max_length=20, null=True, blank=True)
    complemento = models.CharField("Complemento", max_length=255, null=True, blank=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    fechado_em = models.DateTimeField("Fechado em", null=True, blank=True)
    status = models.CharField(
        "Status",
        max_length=3,
        choices=[("ABE", "Aberta"), ("AND", "Em Andamento"), ("FEC", "Fechada")],
    )
    foto = models.ImageField("Foto", upload_to="ocorrencias/", null=True, blank=True)
    cidadao = models.ForeignKey(Cidadao, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
        ordering = ["id"]

    def __str__(self):
        return f"{self.titulo}"
