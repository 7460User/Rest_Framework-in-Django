# Generated by Django 5.0.2 on 2024-05-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pranav_Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('mob', models.IntegerField()),
                ('email', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=101)),
            ],
        ),
    ]
