from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FA
from django.utils.translation import ugettext_lazy as _

from modeltranslation.admin import TabbedTranslationAdmin
# Register your models here.


admin.site.unregister(FlatPage)

@admin.register(FlatPage)
class FlatPageAdmin(TabbedTranslationAdmin, FA):
    pass
