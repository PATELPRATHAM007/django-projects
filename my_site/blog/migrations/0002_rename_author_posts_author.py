# Generated by Django 5.1.1 on 2024-10-16 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='Author',
            new_name='author',
        ),
    ]
