from django import template
from subscribers.forms import SubscriberForm

register = template.Library()


@register.inclusion_tag('subscribers/subscribe_form.html')
def get_subscriber_form():
    return {'form': SubscriberForm()}