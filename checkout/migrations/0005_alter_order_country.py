# Generated by Django 3.2 on 2022-08-15 20:57

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=250),
        ),
    ]
