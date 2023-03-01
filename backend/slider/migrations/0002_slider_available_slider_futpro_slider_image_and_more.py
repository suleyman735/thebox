# Generated by Django 4.1.5 on 2023-01-31 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='futPro',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='image',
            field=models.ImageField(null=True, upload_to='thebox/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='slider',
            name='imgDesc',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='proName',
            field=models.CharField(max_length=15, null=True),
        ),
    ]