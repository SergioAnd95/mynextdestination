from django.views.generic import FormView
from django.http import JsonResponse

from .forms import SubscriberForm
# Create your views here.


class SubscriberFormView(FormView):
    form_class = SubscriberForm
    http_method_names = ['post']

    def form_valid(self, form):
        form.save()
        return JsonResponse({'status': 'success'})

    def form_invalid(self, form):
        return JsonResponse(form.errors)
