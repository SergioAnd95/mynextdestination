from django.conf.urls import url
from django.views.decorators.cache import cache_page


from . import views

urlpatterns = [
    url(r'^category/(?P<slug>[-\w]+)/$', cache_page(60*15)(views.CategoryDetailView.as_view()), name='category_detail'),
    url(r'^resource/(?P<slug>[-\w]+)/$', cache_page(60*30)(views.ResourceDetailView.as_view()), name='resource_detail'),
    url(r'^propose_resource/$', views.ProposeResourceAjaxFormView.as_view(), name='propose_resource'),
]