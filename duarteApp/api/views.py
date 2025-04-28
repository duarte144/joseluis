
from rest_framework import viewsets
from duarteApp.models import Automovil
from duarteApp.api.serializers import AutomovilSerializer


class AutomovilViewSet(viewsets.ModelViewSet):
    queryset = Automovil.objects.all()
    serializer_class = AutomovilSerializer
