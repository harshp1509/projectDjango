# Generated by Django 4.0.5 on 2022-06-24 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_suggestion_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='content',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='suggestion',
            old_name='title',
            new_name='Subject',
        ),
    ]
