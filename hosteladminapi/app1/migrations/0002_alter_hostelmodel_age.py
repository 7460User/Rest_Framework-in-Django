# Generated by Django 5.0.2 on 2024-05-28 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelmodel',
            name='age',
            field=models.IntegerField(),
        ),
    ]
