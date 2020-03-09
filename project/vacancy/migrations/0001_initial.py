# Generated by Django 3.0.2 on 2020-03-09 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Тип документів',
                'verbose_name_plural': 'Типи документів',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Стать',
                'verbose_name_plural': 'Стать',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Тип роботи',
                'verbose_name_plural': 'Типи роботи',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('work_position', models.CharField(blank=True, max_length=1000, null=True)),
                ('work_day', models.CharField(blank=True, max_length=1000, null=True)),
                ('your_duties', models.TextField(blank=True, null=True)),
                ('our_duties', models.TextField(blank=True, null=True)),
                ('duties', models.TextField(blank=True, null=True)),
                ('actual', models.BooleanField(default=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='country', to='service.Country')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='vacancy.DocumetType')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancy.Gender')),
                ('work_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_types', to='vacancy.WorkType')),
            ],
            options={
                'verbose_name': 'Вакансія',
                'verbose_name_plural': 'Вакансії',
            },
        ),
    ]
