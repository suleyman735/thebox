# Generated by Django 4.1.5 on 2023-03-03 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0015_counterselection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesionalsection',
            name='icon',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
