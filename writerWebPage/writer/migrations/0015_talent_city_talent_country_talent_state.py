# Generated by Django 4.0.3 on 2022-03-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0014_talent_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='talent',
            name='city',
            field=models.CharField(default='Manizales', max_length=20),
        ),
        migrations.AddField(
            model_name='talent',
            name='country',
            field=models.CharField(default='Colombia', max_length=20),
        ),
        migrations.AddField(
            model_name='talent',
            name='state',
            field=models.CharField(default='Caldas', max_length=20),
        ),
    ]