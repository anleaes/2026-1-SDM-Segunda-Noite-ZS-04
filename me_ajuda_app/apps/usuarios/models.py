from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    nome = models.CharField("Nome", max_length=50)
    sobrenome = models.CharField("Sobrenome", max_length=50)
    cpf = models.CharField("Cpf", max_length=11)
    email = models.CharField("Email", max_length=50)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["id"]

    def __str__(self):
        return f"{self.nome} - {self.sobrenome}"
