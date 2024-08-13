# Generated by Django 5.1 on 2024-08-11 04:02

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.modulo')),
            ],
        ),
        migrations.CreateModel(
            name='RolPermiso',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.permiso')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.rol')),
            ],
        ),
        migrations.AddField(
            model_name='rol',
            name='permisos',
            field=models.ManyToManyField(through='seguridad.RolPermiso', to='seguridad.permiso'),
        ),
        migrations.CreateModel(
            name='PermisoUsuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.permiso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioRol',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.rol')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguridad.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='roles',
            field=models.ManyToManyField(through='seguridad.UsuarioRol', to='seguridad.rol'),
        ),
    ]
