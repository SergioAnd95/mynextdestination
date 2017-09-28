from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='index'),
    url(r'^search/autocomplete/$', views.autocomplete, name='autocomplete')
]