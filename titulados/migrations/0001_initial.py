# Generated by Django 2.2 on 2020-07-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titulado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('título', models.CharField(blank=True, max_length=254, null=True)),
                ('elo', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
