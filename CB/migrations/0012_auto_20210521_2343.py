# Generated by Django 3.1.5 on 2021-05-21 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CB', '0011_auto_20210521_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followcollege',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
