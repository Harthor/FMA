# Generated by Django 2.2 on 2020-08-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0006_player_elo'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='título',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
