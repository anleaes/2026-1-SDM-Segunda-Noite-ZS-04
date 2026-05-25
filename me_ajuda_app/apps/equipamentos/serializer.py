from .models import Equipamento
from rest_framework import serializers

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'
