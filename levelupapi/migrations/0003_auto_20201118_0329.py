# Generated by Django 3.1.3 on 2020-11-18 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_event_game_gametype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='gamer_type',
            new_name='game_type',
        ),
    ]
