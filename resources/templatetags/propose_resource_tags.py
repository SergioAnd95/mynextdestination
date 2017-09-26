from django import template

from resources.forms import ProposeResourceForm

register = template.Library()


@register.inclusion_tag('resources/propose_form.html')
def get_form():
    return {'form': ProposeResourceForm()}
