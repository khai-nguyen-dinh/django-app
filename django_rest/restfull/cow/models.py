from django.contrib.admin import models
from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=11)
    email = models.EmailField()
    joined = models.DateTimeField(auto_now_add=True, blank=True)

class Post(models.Model):
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    class Meta:
        ordering = ['date_created']
        verbose_name_plural = 'test'
