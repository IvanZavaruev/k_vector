# Generated by Django 3.1.7 on 2021-11-26 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='news_data',
            new_name='news_date',
        ),
    ]
