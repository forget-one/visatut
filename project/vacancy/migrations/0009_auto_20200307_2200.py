# Generated by Django 3.0 on 2020-03-07 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0008_auto_20200307_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='gender',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancy.Gender'),
        ),
    ]
