from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.getAll, name='eventos'),
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^registracion', views.postEvento, name='registracion'),
]
