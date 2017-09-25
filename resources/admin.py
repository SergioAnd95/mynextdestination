from django.contrib import admin

from . import models
# Register your models here.


class RelatedResourceInline(admin.TabularInline):
    model = models.RelatedResources
    fk_name = 'primary'
    raw_id_fields = ['primary', 'recommendation']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):

    def hit_count(self, obj):
        return obj.hit_count.hits

    list_display = ('name', 'link', 'priority', 'hit_count',)
    prepopulated_fields = {'slug': ('name', )}
    inlines = [RelatedResourceInline, ]
    search_fields = ('name',)
    list_filter = ('priority', )