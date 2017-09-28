from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse

from haystack.query import SearchQuerySet

from resources.models import Resource
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['last_resources'] = Resource.objects.all()[:6]
        return ctx


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', '')) [:5]
    suggestion = [[res.name, res.object.get_absolute_url()] for res in sqs]
    ctx = {'result': suggestion}

    return JsonResponse(ctx)
