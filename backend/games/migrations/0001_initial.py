# Generated by Django 2.2.1 on 2019-06-16 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('igdb', models.CharField(max_length=16)),
                ('name', models.CharField(default='default', max_length=255)),
            ],
        ),
    ]
