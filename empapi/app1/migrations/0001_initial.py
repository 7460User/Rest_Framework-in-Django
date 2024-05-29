# Generated by Django 5.0.2 on 2024-05-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('techno', models.CharField(max_length=40)),
                ('collegename', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]