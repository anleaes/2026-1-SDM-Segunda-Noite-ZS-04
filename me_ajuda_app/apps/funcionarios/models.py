from django.db import models
from secretarias.models import Secretaria
from usuarios.models import Usuario


# Create your models here.
class Funcionario(Usuario):
    registro = models.CharField("Registro", max_length=20)
    funcao = models.CharField(
        "Função",
        max_length=3,
        choices=[
            ("TEC", "Técnico"),
            ("GES", "Gestor"),
            ("ANA", "Analista"),
        ],
    )
    ativo = models.BooleanField("Ativo", default=True)
    secretarias = models.ManyToManyField(Secretaria, verbose_name="Secretarias")

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ["id"]

    def __str__(self):
        return super().__str__()
