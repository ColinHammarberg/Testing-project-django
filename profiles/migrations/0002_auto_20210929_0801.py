# Generated by Django 3.2.7 on 2021-09-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='email',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='full_name',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
