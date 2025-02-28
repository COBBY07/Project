# Generated by Django 4.2.11 on 2024-06-26 01:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_alter_video_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/%y', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4.avi', '.mov', '.mkv'])]),
        ),
    ]
