# Generated by Django 3.1.3 on 2020-11-18 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20201118_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='number_of_plyers',
            new_name='number_of_players',
        ),
    ]