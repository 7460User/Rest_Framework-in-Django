# Generated by Django 5.0.2 on 2024-05-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WiproEmpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=20)),
                ('ofclemail', models.CharField(max_length=30)),
                ('techno', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('complocation', models.CharField(max_length=40)),
            ],
        ),
    ]
