# Generated by Django 5.1.2 on 2024-10-19 03:17

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
