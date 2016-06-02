from django.contrib import admin

# Register your models here.
from app.models import Data, NewsWebsite

admin.site.register(Data)
admin.site.register(NewsWebsite)