# Generated by Django 4.1.5 on 2023-02-27 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0006_aboutfront'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutfront',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]