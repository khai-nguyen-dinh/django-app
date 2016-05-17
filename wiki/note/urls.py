from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$',views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^logout/$', views.logout, name='logout'),
]