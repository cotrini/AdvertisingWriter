# Generated by Django 4.0.3 on 2022-03-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0008_talent_email_talent_photographer_talent_writer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
    ]