from copy import deepcopy as copy
from django_jinja import library
import jinja2


@library.global_function
def render_field(field, **kwargs):
    attrs = copy(field.field.widget.attrs)
    field.field.widget.attrs.update(kwargs)
    try:
        return str(field)
    finally:
        for key in kwargs:
            del field.field.widget.attrs[key]
        field.field.widget.attrs.update(attrs)