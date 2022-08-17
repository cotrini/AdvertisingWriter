import email
from enum import unique
from django.db import models
from django.db.models.fields import CharField, URLField, DateField
from django.db.models.fields.files import ImageField
from django.forms import EmailField
from pandas import notnull
from django.utils.safestring import mark_safe



class talent(models.Model):
    fullName = CharField(max_length=100)
    description = CharField(max_length=1000)
    photo1 = ImageField(upload_to='talentsImages')
    photo2 = ImageField(upload_to='talentsImages')
    photo3 = ImageField(upload_to='talentsImages')
    birtdate = DateField()
    facebook = URLField(max_length=200, blank=True)
    instagram = URLField(max_length=200, blank=True)
    youtube = URLField(max_length=200, blank=True)
    phoneNumber = CharField(max_length=12, unique=True, blank=False)
    email = models.EmailField(max_length=100, default='')
    country = CharField(max_length=20, default='Colombia')
    state = CharField(max_length=20, default='Caldas')
    city = CharField(max_length=20, default='Manizales')
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    actor = models.BooleanField(default=False)
    announcer = models.BooleanField(default=False)
    singer = models.BooleanField(default=False)
    dancer = models.BooleanField(default=False)
    writer = models.BooleanField(default=False)
    photographer = models.BooleanField(default=False)

    def talentPhoto(self):
        return mark_safe('<img src="{url}" width="300" height="300" />'.format( url = self.photo.url))

    def __str__(self):
        return self.fullName
