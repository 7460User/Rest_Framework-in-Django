# Generated by Django 5.0.2 on 2024-03-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student_date_alter_student_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
