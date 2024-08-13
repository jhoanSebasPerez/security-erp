from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from seguridad.models import Usuario
from seguridad.serializers import UsuarioSerializer, PermisoSerializer, RolSerializer
from seguridad.services.usuario_service import UsuarioService

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @extend_schema(
        summary="Asignar un rol a un usuario",
        description="Este endpoint asigna un rol específico a un usuario dado, siempre y cuando el rol no haya sido asignado previamente.",
        #request=RolIDSerializer,
        responses={
            200: OpenApiResponse(description='Rol asignado exitosamente.'),
            400: OpenApiResponse(description='El rol ya está asignado a este usuario o los parámetros no son válidos.'),
            404: OpenApiResponse(description='Usuario o rol no encontrado.')
        },
        examples=[
            OpenApiExample(
                'Ejemplo de solicitud',
                description='Ejemplo de cómo enviar una solicitud para asignar un rol a un usuario.',
                value={"rol_id": "id del rol"},
                request_only=True
            ),
        ]
    )
    @action(detail=True, methods=['post'], url_path='asignar-rol')
    def asignar_rol(self, request, pk=None):
        usuario = self.get_object()
        rol_id = request.data.get('rol_id')

        if not rol_id:
            return Response({'error': 'rol_id es requerido.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            UsuarioService.asignar_rol_a_usuario(usuario, rol_id)
            return Response({'success': 'Rol asignado exitosamente.'}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        summary="Asignar un permiso a un usuario",
        description="Este endpoint asigna un permiso específico a un usuario dado, siempre y cuando el permiso no haya sido asignado previamente ni esté cubierto por algún rol del usuario.",
        request=PermisoSerializer,
        responses={
            200: OpenApiResponse(description='Permiso asignado exitosamente.'),
            400: OpenApiResponse(description='El permiso ya está asignado a este usuario o está cubierto por uno de sus roles.'),
            404: OpenApiResponse(description='Usuario o permiso no encontrado.')
        },
        examples=[
            OpenApiExample(
                'Ejemplo de solicitud',
                description='Ejemplo de cómo enviar una solicitud para asignar un permiso a un usuario.',
                value={"permiso_id": "id del permiso"},
                request_only=True
            ),
        ]
    )
    @action(detail=True, methods=['post'], url_path='asignar-permiso')
    def asignar_permiso(self, request, pk=None):
        usuario = self.get_object()
        permiso_id = request.data.get('permiso_id')

        if not permiso_id:
            return Response({'error': 'permiso_id es requerido.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            Usuario.asignar_permiso_a_usuario(usuario, permiso_id)
            return Response({'success': 'Permiso asignado exitosamente.'}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        summary="Listar roles de un usuario",
        description="Este endpoint lista todos los roles asignados a un usuario específico.",
        responses={
            200: RolSerializer(many=True),
            404: OpenApiResponse(description='Usuario no encontrado.')
        }
    )
    @action(detail=True, methods=['get'], url_path='listar-roles')
    def listar_roles(self, request, pk=None):
        usuario = self.get_object()
        roles = UsuarioService.listar_roles(usuario)
        serializer = RolSerializer(roles, many=True)
        return Response(serializer.data) 

    @extend_schema(
        summary="Listar permisos de un usuario",
        description="Este endpoint lista todos los permisos asignados a un usuario, incluyendo los obtenidos a través de roles.",
        responses={
            200: PermisoSerializer(many=True),
            404: OpenApiResponse(description='Usuario no encontrado.')
        }
    )
    @action(detail=True, methods=['get'], url_path='listar-permisos')
    def listar_permisos(self, request, pk=None):
        usuario = self.get_object()
        permisos = UsuarioService.obtener_permisos_de_usuario(usuario)
        serializer = PermisoSerializer(permisos, many=True)
        return Response(serializer.data)