# Generated by Django 3.0 on 2020-03-06 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_auto_20200305_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='slug',
        ),
    ]