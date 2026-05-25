from .models import IntervencaoEquipamento
from rest_framework import serializers

class IntervencaoEquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervencaoEquipamento
        fields = '__all__'

