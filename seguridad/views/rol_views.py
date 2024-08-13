from rest_framework import viewsets
from seguridad.models import Rol
from seguridad.serializers import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
