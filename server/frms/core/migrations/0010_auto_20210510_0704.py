# Generated by Django 3.1.10 on 2021-05-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210510_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='collection',
        ),
        migrations.AlterField(
            model_name='feature',
            name='code',
            field=models.CharField(default='FTV9Z94HA7O5E90T', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='code',
            field=models.CharField(default='LYF4HJ9WBJ2M90X6', max_length=16, unique=True, verbose_name='Code'),
        ),
    ]
