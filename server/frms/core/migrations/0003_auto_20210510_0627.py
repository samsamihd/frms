# Generated by Django 3.1.10 on 2021-05-10 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210510_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='code',
            field=models.CharField(default='FT0EMFCPFRLP8O0X', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='code',
            field=models.CharField(default='LYTJ8ZEDKPTYX7BA', max_length=16, unique=True, verbose_name='Code'),
        ),
    ]