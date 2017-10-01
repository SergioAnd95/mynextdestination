from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email', )
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }