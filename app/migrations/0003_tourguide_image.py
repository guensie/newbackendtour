# Generated by Django 2.0.6 on 2018-07-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180707_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourguide',
            name='image',
            field=models.CharField(default='english', max_length=150),
        ),
    ]
