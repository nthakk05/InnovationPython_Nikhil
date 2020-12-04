from django.db import models

class form(models.Model):
    Name = models.CharField(max_length = 20, blank=True)
    User_ID = models.CharField(max_length=10, blank=True , unique=True)
    Address = models.TextField(max_length = 20, blank=True )

    def __str__(self):
        self.Name