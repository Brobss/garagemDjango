# Generated by Django 4.1.7 on 2023-03-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0002_remove_marca_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='nome',
            field=models.CharField(default='', max_length=50),
        ),
    ]