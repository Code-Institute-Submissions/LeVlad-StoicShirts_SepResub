# Generated by Django 3.2 on 2022-08-28 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_alter_quote_custom_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='type',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='custom_name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quotes',
            field=models.TextField(max_length=254, null=True),
        ),
    ]
