# Generated by Django 2.2 on 2020-07-22 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0003_remove_player_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='titulo',
        ),
    ]