# Generated by Django 3.1.6 on 2021-02-21 12:39

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='default_country',
            field=django_countries.fields.CountryField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_street_address1',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='default_town_or_city',
            field=models.CharField(max_length=40, null=True),
        ),
    ]