# Generated by Django 3.1.10 on 2021-05-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210510_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='code',
            field=models.CharField(default='FTHQHIZR400PUNYM', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='code',
            field=models.CharField(default='LYPKKJI878X2GKAI', max_length=16, unique=True, verbose_name='Code'),
        ),
    ]
