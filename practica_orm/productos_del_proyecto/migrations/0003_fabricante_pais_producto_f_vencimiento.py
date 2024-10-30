# Generated by Django 5.1.1 on 2024-10-16 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_del_proyecto', '0002_fabricante_producto_fabricante'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricante',
            name='pais',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='f_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
