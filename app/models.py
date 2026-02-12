from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='media/', default='media/example.png', blank=True)