from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^$', cache_page(60*15)(views.HomeView.as_view()), name='index'),
    url(r'^search/autocomplete/$', views.autocomplete, name='autocomplete')
]