# Generated by Django 2.0.6 on 2018-07-07 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_tourguide_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourguide',
            name='user',
        ),
    ]