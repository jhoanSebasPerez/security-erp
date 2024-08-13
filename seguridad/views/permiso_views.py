from rest_framework import viewsets
from seguridad.models import Permiso
from seguridad.serializers import PermisoSerializer

class PermisoViewSet(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
