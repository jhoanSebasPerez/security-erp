from seguridad.models import Rol, Permiso, UsuarioRol, PermisoUsuario

class UsuarioService:
    @staticmethod
    def listar_roles(usuario):
        return Rol.objects.filter(usuariorol__usuario=usuario)

    @staticmethod
    def asignar_rol_a_usuario(usuario, rol_id):
        try:
            rol = Rol.objects.get(id=rol_id)
        except Rol.DoesNotExist:
            raise ValueError("Rol no encontrado.")

        if UsuarioRol.objects.filter(usuario=usuario, rol=rol).exists():
            raise ValueError("El rol ya está asignado a este usuario.")

        UsuarioRol.objects.create(usuario=usuario, rol=rol)

    @staticmethod
    def asignar_permiso_a_usuario(usuario, permiso_id):
        try:
            permiso = Permiso.objects.get(id=permiso_id)
        except Permiso.DoesNotExist:
            raise ValueError("Permiso no encontrado.")

        if PermisoUsuario.objects.filter(usuario=usuario, permiso=permiso).exists():
            raise ValueError("El permiso ya está asignado directamente a este usuario.")

        roles_con_permiso = Rol.objects.filter(usuariorol__usuario=usuario, permisos=permiso)
        if roles_con_permiso.exists():
            raise ValueError("El permiso ya está cubierto por uno de los roles del usuario.")

        PermisoUsuario.objects.create(usuario=usuario, permiso=permiso)
    
    from seguridad.models import Usuario, Permiso, PermisoUsuario, Rol

    @staticmethod
    def obtener_permisos_de_usuario(usuario):
        # Obtener los permisos asignados directamente al usuario
        permisos_directos = Permiso.objects.filter(permisousuario__usuario=usuario)

        # Obtener los permisos que el usuario tiene a través de sus roles
        permisos_por_roles = Permiso.objects.filter(rol__usuariorol__usuario=usuario).distinct()

        # Unir ambos conjuntos de permisos
        permisos_totales = permisos_directos.union(permisos_por_roles)

        return permisos_totales