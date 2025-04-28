
from rest_framework import serializers
from duarteApp.models import Automovil

class AutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovil
        fields = '__all__'
