# Generated by Django 4.0.4 on 2022-05-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vollclub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='thumbnails/default.png', upload_to='thumbnails'),
        ),
    ]
