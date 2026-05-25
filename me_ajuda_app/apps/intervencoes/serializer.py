from .models import Intervencao
from rest_framework import serializers

class IntervencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervencao
        fields = '__all__'
