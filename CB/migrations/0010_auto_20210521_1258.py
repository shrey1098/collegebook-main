# Generated by Django 3.1.5 on 2021-05-21 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CB', '0009_auto_20210515_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followcollege',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CB.college', to_field='college_name'),
        ),
    ]
