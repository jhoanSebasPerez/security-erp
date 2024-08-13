from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Usuario, Rol, Permiso, Modulo, PermisoUsuario, UsuarioRol, RolPermiso

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password']  # Incluir el campo 'password' para entrada
        extra_kwargs = {'password': {'write_only': True}}  # Marcar el campo 'password' como solo escritura

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UsuarioSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super(UsuarioSerializer, self).update(instance, validated_data)

class PermisoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoUsuario
        fields = '__all__'

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioRol
        fields = '__all__'

class RolPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolPermiso
        fields = '__all__'