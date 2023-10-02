from django.db import models

# Create your models here.

from django.core import validators
from django import forms

def check_for_a(data):
    if data[0].lower()=='a':
        raise forms.ValidationError('Name starts with A')


class Topic(models.Model):
    topic_name = models.CharField(max_length=100,primary_key=True,validators=[check_for_a])

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,validators=[validators.MinLengthValidator(6)])
    url = models.URLField()

    def __str__(self):
        return self.name


