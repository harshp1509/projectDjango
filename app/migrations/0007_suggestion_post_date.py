# Generated by Django 4.0.5 on 2022-06-24 05:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_content_suggestion_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='post_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
