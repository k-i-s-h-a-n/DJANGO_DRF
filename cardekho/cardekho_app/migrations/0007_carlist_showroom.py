# Generated by Django 5.0.6 on 2024-06-26 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardekho_app', '0006_showroomlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='showroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showrooms', to='cardekho_app.showroomlist'),
        ),
    ]
