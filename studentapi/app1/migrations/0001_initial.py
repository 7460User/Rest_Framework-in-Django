# Generated by Django 5.0.2 on 2024-03-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('mobile', models.IntegerField(max_length=13)),
                ('address', models.CharField(max_length=120)),
                ('about', models.CharField(max_length=120)),
            ],
        ),
    ]
