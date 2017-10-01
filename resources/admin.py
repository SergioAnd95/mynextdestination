from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from . import models
# Register your models here.


class RelatedResourceInline(admin.TabularInline):
    model = models.RelatedResources
    fk_name = 'primary'
    raw_id_fields = ['primary', 'recommendation']


class CategoryAdmin(TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('name', )}


class ResourceAdmin(TabbedTranslationAdmin):

    def hit_count(self, obj):
        return obj.hit_count.hits

    list_display = ('name', 'link', 'priority', 'hit_count',)
    prepopulated_fields = {'slug': ('name', )}
    inlines = [RelatedResourceInline, ]
    search_fields = ('name',)
    list_filter = ('priority', )


@admin.register(models.ProposeResource)
class ProposeResourceAdmin(admin.ModelAdmin):
    list_display = ('resource_name', 'resource_url', 'when_created')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Resource, ResourceAdmin)