# Generated by Django 2.2.1 on 2019-05-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_game_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='default', max_length=255),
        ),
    ]