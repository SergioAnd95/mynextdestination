from django import template
from resources.models import Category

register = template.Library()


@register.assignment_tag
def get_all_categories():
    return Category.objects.all()


@register.filter
def split_array(array, count):
    return [array[i*count:i*count+count] for i in range(len(array)//count+1)]