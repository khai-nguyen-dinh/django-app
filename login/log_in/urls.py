from django.conf.urls import url, include
from log_in import views

urlpatterns = [
    url(r'^sign_in/$',views.sign_in,name="signin"),
    url(r'^sign_out/$', views.sign_out, name="sign_out"),
]
