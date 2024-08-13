from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from seguridad.models import Permiso, models
from seguridad.permissions_config import url_permission_map

class PermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Antes de manejar la solicitud, validamos los permisos
        response = self.process_request(request)
        if response:
            return response

        # Pasamos al siguiente middleware o la vista si no hay problema
        response = self.get_response(request)
        return response

    def process_request(self, request):
        # Excluir rutas relacionadas con Swagger
        if request.path.startswith('/api/schema/') or request.path.startswith('/api/token/'):
            return None

        # Autenticación del usuario utilizando JWT
        user = None
        try:
            jwt_authenticator = JWTAuthentication()
            user, _ = jwt_authenticator.authenticate(request)
        except Exception:
            return JsonResponse({'detail': 'Invalid token or no token provided'}, status=status.HTTP_401_UNAUTHORIZED)

        if user is None:
            return JsonResponse({'detail': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

        # Validar si la ruta solicitada requiere un permiso específico
        for url, permission_codename in url_permission_map.items():
            if request.path.startswith(url):
                # Verificamos si el usuario tiene el permiso
                if not self.user_has_permission(user, permission_codename):
                    return JsonResponse({'detail': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

        # Si no se requiere permiso o si el usuario tiene el permiso, no hacemos nada
        return None

    def user_has_permission(self, user, permission_codename):
        # Verificar si el usuario tiene el permiso directamente o a través de sus roles
        has_permission = Permiso.objects.filter(
            models.Q(permisousuario__usuario=user) | 
            models.Q(rol__usuariorol__usuario=user), 
            code=permission_codename
        ).exists()

        return has_permission