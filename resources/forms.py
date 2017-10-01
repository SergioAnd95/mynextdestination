from django import forms
from django.utils.translation import ugettext_lazy as _

from haystack.query import SearchQuerySet as SQS

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


class CategoryOrderForm(forms.Form):
    class OrderByChoices:
        BY_DATE = '-when_created'
        BY_NAME = '-name'

        CHOICES = (
            (BY_NAME, _('By name')),
            (BY_DATE, _('By date')),
        ) 
    
    order = forms.ChoiceField(
        choices=OrderByChoices.CHOICES, 
        required=False, 
        label=_('Order'),
        initial=OrderByChoices.BY_DATE
    )

    def __init__(self, *args, **kwargs):
        self.category = kwargs.pop('category', None)
        super().__init__(*args, **kwargs)
    
    def search(self):
        """
        Method to order resource
        """
        sqs = SQS().all()
        if self.category:
            sqs = SQS().filter(categories=self.category.pk)
        
        if self.is_valid() and 'order' in self.cleaned_data:
            sqs = sqs.order_by('-priority', self.cleaned_data['order'])
        else:
            sqs = sqs.order_by('-priority', '-hits', self.OrderByChoices.BY_DATE)
        return sqs