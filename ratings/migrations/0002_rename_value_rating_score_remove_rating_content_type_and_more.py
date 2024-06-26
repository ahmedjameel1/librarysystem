# Generated by Django 5.0.6 on 2024-06-26 13:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='value',
            new_name='score',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='object_id',
        ),
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
