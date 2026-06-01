from .models import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    tipo_usuario = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ["id", "nome", "sobrenome", "cpf", "email", "user", "tipo_usuario"]

    def get_tipo_usuario(self, obj):
        if hasattr(obj, "funcionario"):
            return "funcionario"
        elif hasattr(obj, "cidadao"):
            return "cidadao"
        return "usuario_base"
