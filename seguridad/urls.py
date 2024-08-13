from django.urls import include, path
from rest_framework import routers
from seguridad.views import UsuarioViewSet, RolViewSet, PermisoViewSet, ModuloViewSet


router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'roles', RolViewSet)
router.register(r'permisos', PermisoViewSet)
router.register(r'modulos', ModuloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]