# Generated by Django 4.2.2 on 2023-07-29 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addressapp', '0008_alter_usercontact_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usercontact',
            name='user1',
        ),
    ]
