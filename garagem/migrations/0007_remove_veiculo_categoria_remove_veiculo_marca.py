# Generated by Django 4.2.4 on 2023-08-21 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0006_alter_veiculo_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='marca',
        ),
    ]
