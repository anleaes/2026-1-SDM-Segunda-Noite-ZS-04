from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobrenome', max_length=50)
    cpf = models.CharField('Cpf', max_length=11)
    email = models.CharField('Email', max_length=50)


