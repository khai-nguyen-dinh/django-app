from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^(?P<title>\w+)/$', views.index, name="index"),
    url(r'^(?P<title>\w+)/edit/$', views.edit,name="edit"),
    url(r'^(?P<title>\w+)/save/$', views.save, name="save"),
]
