# Generated by Django 2.2.7 on 2019-12-12 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel_renta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renta',
            name='fecha',
            field=models.DateField(verbose_name='fecha'),
        ),
    ]