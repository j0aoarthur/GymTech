# Generated by Django 4.2.3 on 2023-08-09 02:20

import cadastro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_alter_person_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profileImage',
            field=models.ImageField(blank=True, upload_to="profileImage/", verbose_name='Imagem de perfil'),
        ),
    ]
