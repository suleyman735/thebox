# Generated by Django 4.1.5 on 2023-02-27 15:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0007_aboutfront_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutExprience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('description', models.TextField(max_length=280, null=True)),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutheader',
            name='available',
        ),
        migrations.RemoveField(
            model_name='aboutheader',
            name='available1',
        ),
        migrations.RemoveField(
            model_name='aboutheader',
            name='image',
        ),
        migrations.RemoveField(
            model_name='aboutheader',
            name='link',
        ),
    ]
