# Generated by Django 4.1.7 on 2023-03-13 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='nome',
        ),
    ]