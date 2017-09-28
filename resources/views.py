from django.views.generic import DetailView, FormView
from django.http import JsonResponse

from hitcount.views import HitCountDetailView

from .models import Category, Resource
from .forms import ProposeResourceForm
# Create your views here.


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'resources/category.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('resources')


class ResourceDetailView(HitCountDetailView):
    model = Resource
    count_hit = True
    context_object_name = 'resource'
    template_name = 'resources/resource.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related('tags')


class ProposeResourceAjaxFormView(FormView):
    form_class = ProposeResourceForm
    template_name = 'resources/propose_form.html'
    http_method_names = ['post']

    def form_valid(self, form):
        form.save()
        return JsonResponse({'status':'ok'})

    def form_invalid(self, form):
        return JsonResponse(form.errors)

