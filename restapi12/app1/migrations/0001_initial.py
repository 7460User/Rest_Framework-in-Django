# Generated by Django 5.0.2 on 2024-04-16 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('companyname', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=120)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Model2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('techno', models.CharField(max_length=50)),
                ('officialemail', models.CharField(max_length=40)),
            ],
        ),
    ]