# Generated by Django 4.1.3 on 2022-11-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_imovel_ativacao_alter_imovel_atualizacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='check_out',
            field=models.DateField(),
        ),
    ]
