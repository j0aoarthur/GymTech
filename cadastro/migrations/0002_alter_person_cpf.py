# Generated by Django 4.2.3 on 2023-08-01 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]
