from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Equipamento(models.Model):
    nome = models.CharField("Nome", max_length=50)
    descricao = models.CharField("Descrição", max_length=100)
    disponivel = models.BooleanField("Disponível", default=True)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"
        ordering = ["id"]

    def __str__(self):
        return f"{self.nome} - R${self.preco}"
