# Generated by Django 3.1.10 on 2021-05-10 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210510_0652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='collection',
        ),
        migrations.AlterField(
            model_name='feature',
            name='code',
            field=models.CharField(default='FTPABXQFQ2TD8SM4', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='code',
            field=models.CharField(default='LY2RTC5O8M1AUJOO', max_length=16, unique=True, verbose_name='Code'),
        ),
    ]
