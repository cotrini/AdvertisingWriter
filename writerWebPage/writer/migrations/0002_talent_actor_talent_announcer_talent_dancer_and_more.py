# Generated by Django 4.0.3 on 2022-03-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='actor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talent',
            name='announcer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talent',
            name='dancer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='talent',
            name='singer',
            field=models.BooleanField(default=False),
        ),
    ]
