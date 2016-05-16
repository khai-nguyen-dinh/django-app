from django.contrib import admin

from note.models import Post
from .views import User

# Register your models here.
admin.site.register(User)
admin.site.register(Post)