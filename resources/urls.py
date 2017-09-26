from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/(?P<slug>[-\w]+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^resource/(?P<slug>[-\w]+)/$', views.ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^propose_resource/$', views.ProposeResourceFormView.as_view(), name='propose_resource'),
]