from django.db import models

from django.urls import reverse

from django import forms
# Create your models here.

class Blog (models.Model):
    AuthorName = models.CharField(max_length = 50,)
    Title = models.CharField(max_length = 100,)
    Content = models.CharField(max_length = 1000,)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwarges = {'pk':self.pk})

