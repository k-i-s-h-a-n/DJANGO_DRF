# Generated by Django 5.0.6 on 2024-06-24 09:35

import cardekho_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardekho_app', '0004_carlist_chasisnumber_carlist_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlist',
            name='chasisNumber',
            field=models.CharField(max_length=100, null=True, validators=[cardekho_app.models.alphanumeric]),
        ),
    ]
