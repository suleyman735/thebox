# Generated by Django 4.1.5 on 2023-02-27 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0004_delete_aboutback_aboutpage_available1_aboutpage_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutPage',
            new_name='AboutHeader',
        ),
    ]