# Generated by Django 3.2.7 on 2022-01-03 12:19

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210929_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='default_country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='default_county',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='default_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='default_full_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='default_phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='default_postcode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='default_street_address',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='default_town_or_city',
            field=models.CharField(max_length=40, null=True),
        ),
    ]