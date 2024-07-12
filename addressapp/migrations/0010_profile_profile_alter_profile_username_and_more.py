# Generated by Django 4.2.2 on 2023-07-29 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addressapp', '0009_remove_profile_user_remove_usercontact_user1'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usercontact',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='addressapp.profile'),
        ),
    ]
