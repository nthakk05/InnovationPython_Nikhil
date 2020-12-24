from django.contrib import admin
from .models import Blog
from django.forms import TextInput, Textarea
# Register your models here.
from django.contrib import admin
from django.db import models
from django.forms import TextInput

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # Django enforces maximum field length of 14 onto 'title' field when user is editing in the change form
        models.CharField: {'widget': TextInput(attrs={'size':'500'})},
        }



admin.site.register(Blog,BlogAdmin)
