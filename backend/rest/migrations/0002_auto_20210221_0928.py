# Generated by Django 3.1.7 on 2021-02-21 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoList',
            new_name='Todo',
        ),
    ]