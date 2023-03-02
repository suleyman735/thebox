# Generated by Django 4.1.5 on 2023-03-02 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0013_postimage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='About.aboutexprience'),
        ),
        migrations.CreateModel(
            name='ProfesionalSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField(max_length=280, null=True)),
                ('smallDescription', models.TextField(max_length=280, null=True)),
                ('icon', models.FileField(upload_to='images/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ProfesionalSection', to='About.aboutexprience')),
            ],
        ),
    ]
