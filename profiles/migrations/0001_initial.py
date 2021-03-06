# Generated by Django 3.2 on 2022-07-21 16:22

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('default_postcode', models.CharField(blank=True, max_length=10, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=32, null=True)),
                ('default_street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
    ]
