# Generated by Django 2.0.6 on 2018-07-12 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_tour_tour_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='tour_guide',
            field=models.ForeignKey(default='13', on_delete=django.db.models.deletion.CASCADE, to='app.TourGuide'),
        ),
    ]
