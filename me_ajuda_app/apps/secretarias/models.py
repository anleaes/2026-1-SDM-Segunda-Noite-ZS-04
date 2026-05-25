from django.db import models


# Create your models here.
class Secretaria(models.Model):
    nome = models.CharField("Nome", max_length=50)
    sigla = models.CharField("Sigla", max_length=10)
    descricao = models.CharField("Descricao", max_length=200)
    site = models.CharField("Site", max_length=200)

    class Meta:
        verbose_name = "Secretaria"
        verbose_name_plural = "Secretarias"
        ordering = ["id"]

    def __str__(self):
        return f"{self.sigla} - {self.nome}"
