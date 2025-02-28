# Generated by Django 4.2.11 on 2024-06-26 01:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default='SOME STRING', max_length=140),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(default='video/placeholder.mp4', upload_to='video/%y', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4.avi', '.mov', '.mkv'])]),
        ),
    ]
