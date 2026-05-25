from .models import Protocolo
from rest_framework import serializers

class ProtocoloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocolo
        fields = '__all__'