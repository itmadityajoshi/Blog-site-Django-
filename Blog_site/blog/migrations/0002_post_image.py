# Generated by Django 5.1.1 on 2024-09-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='blogsite/images'),
        ),
    ]
