# Generated by Django 5.1.2 on 2024-10-22 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_stafflogin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='users',
            new_name='user',
        ),
    ]
