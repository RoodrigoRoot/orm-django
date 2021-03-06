# Generated by Django 3.1.5 on 2021-04-28 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True)),
                ('fecha_crea', models.DateTimeField(auto_now_add=True)),
                ('fecha_modifica', models.DateTimeField(auto_now=True)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
