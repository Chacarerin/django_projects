# Generated by Django 5.1.2 on 2024-10-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_alter_tarea_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contador', models.IntegerField(default=0)),
            ],
        ),
    ]
