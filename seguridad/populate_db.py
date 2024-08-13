from seguridad.models import Modulo, Permiso, Rol, Usuario, UsuarioRol, RolPermiso, PermisoUsuario
from django.contrib.auth.hashers import make_password


def run():
    # Crear Modulos
    modulo_hr = Modulo.objects.create(name="Recursos Humanos", description="Módulo de gestión de recursos humanos")
    modulo_finance = Modulo.objects.create(name="Finanzas", description="Módulo de gestión financiera")
    
    # Crear Permisos
    permiso_read_hr = Permiso.objects.create(name="Leer Recursos Humanos", code="read_hr", modulo=modulo_hr)
    permiso_write_hr = Permiso.objects.create(name="Escribir Recursos Humanos", code="write_hr", modulo=modulo_hr)
    permiso_read_finance = Permiso.objects.create(name="Leer Finanzas", code="read_finance", modulo=modulo_finance)
    permiso_write_finance = Permiso.objects.create(name="Escribir Finanzas", code="write_finance", modulo=modulo_finance)
    
    # Crear Roles
    rol_admin = Rol.objects.create(name="Administrador")
    rol_hr_manager = Rol.objects.create(name="Gerente de Recursos Humanos")
    
    # Asignar permisos a roles
    RolPermiso.objects.create(rol=rol_admin, permiso=permiso_read_hr)
    RolPermiso.objects.create(rol=rol_admin, permiso=permiso_write_hr)
    RolPermiso.objects.create(rol=rol_admin, permiso=permiso_read_finance)
    RolPermiso.objects.create(rol=rol_admin, permiso=permiso_write_finance)
    
    RolPermiso.objects.create(rol=rol_hr_manager, permiso=permiso_read_hr)
    RolPermiso.objects.create(rol=rol_hr_manager, permiso=permiso_write_hr)
    
    # Crear Usuarios
    usuario_admin = Usuario.objects.create(
        username="admin",
        email="admin@example.com",
        password=make_password("adminpassword")
    )
    
    usuario_hr_manager = Usuario.objects.create(
        username="hr_manager",
        email="hr_manager@example.com",
        password=make_password("hrmanagerpassword")
    )
    
    # Asignar roles a usuarios
    UsuarioRol.objects.create(usuario=usuario_admin, rol=rol_admin)
    UsuarioRol.objects.create(usuario=usuario_hr_manager, rol=rol_hr_manager)
    
    # Asignar permisos adicionales a usuarios
    PermisoUsuario.objects.create(usuario=usuario_admin, permiso=permiso_read_hr)
    
    print("Datos precargados exitosamente")