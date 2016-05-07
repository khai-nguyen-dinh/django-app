from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 20, unique = True)
	content = models.TextField()
	def __str__(self):
		return self.title
