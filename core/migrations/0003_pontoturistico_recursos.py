# Generated by Django 4.0.6 on 2022-07-23 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0001_initial'),
        ('core', '0002_alter_pontoturistico_aprovado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='recursos',
            field=models.ManyToManyField(to='recursos.recurso'),
        ),
    ]
