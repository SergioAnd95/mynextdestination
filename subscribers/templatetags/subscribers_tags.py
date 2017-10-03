from django import template

from django_jinja import library
import jinja2

from subscribers.forms import SubscriberForm

register = template.Library()


@register.inclusion_tag('subscribers/subscribe_form.html')
def get_subscriber_form():
    return {'form': SubscriberForm()}


@library.global_function
@library.render_with('subscribers/subscribe_form.html')
def jinja2_get_subscriber_form():
    return {'form': SubscriberForm()}