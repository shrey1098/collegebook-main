# Generated by Django 3.1.5 on 2021-04-30 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CB', '0006_auto_20210430_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswers',
            name='college',
        ),
    ]