from modeltranslation.translator import register, TranslationOptions

from .models import Category, Resource


@register(Category)
class CategoryTranslation(TranslationOptions):
    """
    Translation settings for Category model
    """
    fields = ('name', )


@register(Resource)
class ResourceTranslation(TranslationOptions):
    """
    Translation settings for Resource model
    """
    fields = ('name', 'intro_text', 'full_text')