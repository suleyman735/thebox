# Generated by Django 4.1.5 on 2023-01-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Navbar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbarlogo',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]