# Generated by Django 4.2.2 on 2023-07-28 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addressapp', '0003_rename_password1_profile_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
