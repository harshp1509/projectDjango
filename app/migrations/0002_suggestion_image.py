# Generated by Django 4.0.5 on 2022-06-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='image',
            field=models.ImageField(default='', upload_to='app/images'),
        ),
    ]
