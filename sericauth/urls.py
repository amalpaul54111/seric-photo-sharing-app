from django.conf.urls import url
from . import views
from django import contrib
from django.urls import include
app_name = 'sericauth'

urlpatterns = [
    url(r'^registration', views.test),
    url(r'^user_home/', views.user_home),
    url(r'^test', views.test, name='test'),
    url(r'^login_user', views.login_user, name='login_user')
    ]