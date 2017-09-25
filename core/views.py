from django.shortcuts import render
from django.views.generic import TemplateView

from resources.models import Resource
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['last_resources'] = Resource.objects.all()[:6]
        return ctx