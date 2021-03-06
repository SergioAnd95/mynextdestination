"""mynextdestination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.flatpages import views

urlpatterns = i18n_patterns(
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^', include('resources.urls', namespace='resources')),
    url(r'^search/', include('haystack.urls')),
    url(r'^subscribe/', include('subscribers.urls', namespace='subscribers')),
    url(r'^pages/(?P<url>.*)$', views.flatpage, name='flatpage'),
    url(r'^froala_editor/', include('froala_editor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)