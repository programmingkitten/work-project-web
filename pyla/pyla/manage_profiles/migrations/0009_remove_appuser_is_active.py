# Generated by Django 4.0.3 on 2022-04-13 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_profiles', '0008_appuser_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='is_active',
        ),
    ]
