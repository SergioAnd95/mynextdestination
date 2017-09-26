from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import ProposeResource, Category


class ProposeResourceForm(forms.ModelForm):
    category = forms.ModelChoiceField(Category.objects.all(), empty_label=_('Chose category'), required=False)
    class Meta:
        model = ProposeResource
        fields = '__all__'

        widgets = {
            'resource_name': forms.TextInput(attrs={'placeholder':_('Resource name')}),
            'resource_url' : forms.URLInput(attrs={'placeholder': _('Resource URL')}),
            'description': forms.Textarea(attrs={'placeholder': _('Description')})
        }