# Generated by Django 3.1.10 on 2021-05-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210510_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='attendant',
            field=models.CharField(default='John Doe', max_length=128, verbose_name='Attendant'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feature',
            name='phone',
            field=models.CharField(default='09185175516', max_length=128, verbose_name='Phone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='code',
            field=models.CharField(default='FT9I6JV4LBIXY0X3', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='code',
            field=models.CharField(default='LYE9P1ZUT3WJJIUT', max_length=16, unique=True, verbose_name='Code'),
        ),
    ]
