# Generated by Django 5.1 on 2024-08-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wipro_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=120)),
                ('campanyname', models.CharField(max_length=202)),
                ('empmail', models.EmailField(max_length=254)),
                ('empid', models.IntegerField()),
                ('location', models.CharField(max_length=40)),
            ],
        ),
    ]
