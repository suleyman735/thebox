# Generated by Django 4.1.5 on 2023-03-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0011_postimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postimage',
            old_name='images',
            new_name='image',
        ),
    ]
