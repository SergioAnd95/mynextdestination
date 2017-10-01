from django.conf.urls import url

from .views import SubscriberFormView

urlpatterns = [
    url(r'^create_subscriber/$', SubscriberFormView.as_view(), name='create_subscriber')
]