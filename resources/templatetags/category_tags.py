from django import template
from resources.models import Category

from django_jinja import library
import jinja2

register = template.Library()


@register.assignment_tag
def get_all_categories():
    return Category.objects.all()


@library.global_function
def jinja2_get_all_categories():
    return Category.objects.all()


@register.filter
def split_array(array, count):
    return [array[i*count:i*count+count] for i in range(len(array)//count+1)]


@library.filter
@jinja2.contextfilter
def jinja2_split_array(ctx, array, count):
    print([array[i*count:i*count+count] for i in range(len(array)//count+1)])
    return [array[i*count:i*count+count] for i in range(len(array)//count+1)]