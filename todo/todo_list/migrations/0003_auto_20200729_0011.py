# Generated by Django 3.0.8 on 2020-07-29 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_todo_complete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user',
            new_name='author',
        ),
    ]