# Generated by Django 2.0.6 on 2018-07-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tourguide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourguide',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
