# Generated by Django 5.0.2 on 2024-05-10 06:58

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
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('mobile', models.IntegerField()),
                ('district', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]
