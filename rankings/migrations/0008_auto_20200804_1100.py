# Generated by Django 2.2 on 2020-08-04 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0007_player_título'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='título',
            new_name='titulo',
        ),
    ]
