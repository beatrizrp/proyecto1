# Generated by Django 2.0.4 on 2018-04-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fightgame', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='fighters',
            field=models.ManyToManyField(to='fightgame.Fighter', verbose_name='Luchadores'),
        ),
    ]