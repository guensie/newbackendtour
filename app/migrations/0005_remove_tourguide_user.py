# Generated by Django 2.0.6 on 2018-07-07 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180707_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourguide',
            name='user',
        ),
    ]
