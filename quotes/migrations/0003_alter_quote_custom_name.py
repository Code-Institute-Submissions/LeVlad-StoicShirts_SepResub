# Generated by Django 3.2 on 2022-08-28 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20220828_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='custom_name',
            field=models.CharField(max_length=120),
        ),
    ]
