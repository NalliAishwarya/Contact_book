# Generated by Django 4.2.2 on 2023-07-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressapp', '0002_rename_customuser_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='password1',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
