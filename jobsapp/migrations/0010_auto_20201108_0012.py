# Generated by Django 3.0.7 on 2020-11-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0009_auto_20201108_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
