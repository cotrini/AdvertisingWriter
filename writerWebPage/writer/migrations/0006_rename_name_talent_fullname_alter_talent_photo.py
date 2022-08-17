# Generated by Django 4.0.3 on 2022-03-28 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0005_alter_talent_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talent',
            old_name='name',
            new_name='fullName',
        ),
        migrations.AlterField(
            model_name='talent',
            name='photo',
            field=models.ImageField(upload_to='media/talents/images'),
        ),
    ]
