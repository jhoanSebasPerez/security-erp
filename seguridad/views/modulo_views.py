from rest_framework import viewsets
from seguridad.models import Modulo
from seguridad.serializers import ModuloSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer