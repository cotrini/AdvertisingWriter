# Generated by Django 4.0.3 on 2022-03-28 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='talent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(upload_to='talents/images')),
                ('birtdate', models.DateField()),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
            ],
        ),
    ]
