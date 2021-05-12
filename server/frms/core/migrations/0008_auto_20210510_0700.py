# Generated by Django 3.1.10 on 2021-05-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210510_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='collection',
        ),
        migrations.AlterField(
            model_name='feature',
            name='code',
            field=models.CharField(default='FTM7V8XM7AWUZ52F', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='code',
            field=models.CharField(default='LYMCU909I0GQKKFE', max_length=16, unique=True, verbose_name='Code'),
        ),
    ]
