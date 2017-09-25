from django.shortcuts import render
from django.views.generic import DetailView

from hitcount.views import HitCountDetailView

from .models import Category, Resource
# Create your views here.


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category.html'


class ResourceDetailView(HitCountDetailView):
    model = Resource
    count_hit = True
    context_object_name = 'resource'
    template_name = 'resource.html'