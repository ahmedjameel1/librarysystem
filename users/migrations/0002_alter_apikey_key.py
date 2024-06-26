# Generated by Django 5.0.6 on 2024-06-26 18:33

import secrets
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apikey',
            name='key',
            field=models.CharField(default=secrets.token_urlsafe, max_length=64, unique=True),
        ),
    ]
