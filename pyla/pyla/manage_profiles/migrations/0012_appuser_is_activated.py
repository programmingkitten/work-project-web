# Generated by Django 4.0.3 on 2022-07-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_profiles', '0011_profile_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]
