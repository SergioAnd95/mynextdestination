from django import template

from django_jinja import library

from resources.forms import ProposeResourceForm

register = template.Library()


@register.inclusion_tag('resources/propose_form.html')
def get_form():
    return {'form': ProposeResourceForm()}


@library.global_function
@library.render_with('resources/propose_form.html')
def jinja2_get_form():
    return {'form': ProposeResourceForm()}