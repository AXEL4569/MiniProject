# Generated by Django 3.2.13 on 2022-07-01 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketApp', '0002_auto_20220630_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gigs',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
    ]