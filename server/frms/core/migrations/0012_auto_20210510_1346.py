# Generated by Django 3.1.10 on 2021-05-10 13:46

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0011_auto_20210510_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='code',
            field=models.CharField(default='FT8KGYZHY4SOET28', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='code',
            field=models.CharField(default='LY6K8U0RL4D3A6B2', max_length=16, unique=True, verbose_name='Code'),
        ),
        migrations.CreateModel(
            name='FloodPlain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('happened_at', models.DateTimeField(blank=True, null=True, verbose_name='Happened_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Flood Plain',
                'verbose_name_plural': 'Flood Plain',
            },
        ),
    ]