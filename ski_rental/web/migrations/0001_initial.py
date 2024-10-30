# Generated by Django 5.1.2 on 2024-10-30 01:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('imagen', models.URLField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('arrendado', 'Arrendado'), ('mantenimiento', 'Mantenimiento')], max_length=45)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='web.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('observacion', models.TextField(blank=True, null=True)),
                ('danado', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriendos', to=settings.AUTH_USER_MODEL)),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriendos', to='web.equipo')),
            ],
        ),
    ]
