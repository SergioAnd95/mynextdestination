from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

from taggit.managers import TaggableManager

from hitcount.models import HitCountMixin, HitCount

# Create your models here.


@python_2_unicode_compatible
class ResourceManager(models.Manager):
    def ordering_stage(self):
        return self.order_by('-priority', 'hit_count_generic__hits', '-when_created')


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_('Slug'))

    @permalink
    def get_absolute_url(self):
        return 'resources:category_detail', (self.slug, )

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Resource(models.Model, HitCountMixin):

    class PriorityChoices:

        LOW_PRIORITY = 0
        MEDIUM_PRIORITY = 1
        HIGH_PRIORITY = 2

        CHOICES = (
            (LOW_PRIORITY, _('Low')),
            (MEDIUM_PRIORITY, _('Medium')),
            (HIGH_PRIORITY, _('High'))
        )

    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'))
    main_image = models.ImageField(upload_to='resources')
    intro_text = models.TextField(_('Introduction text'))
    text = models.TextField(_('Text'))
    link = models.URLField(_('Site link'))
    priority = models.PositiveSmallIntegerField(_('Priority'), choices=PriorityChoices.CHOICES)
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'), related_name='resources')
    when_created = models.DateTimeField(_('When created'), auto_now_add=True)
    tags = TaggableManager(verbose_name=_('Tags'), blank=True)

    related_items = models.ManyToManyField(
        'resources.Resource',
        through='resources.RelatedResources',
        blank=True,
        verbose_name=_('Related resources')
    )

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    objects = ResourceManager()

    @permalink
    def get_absolute_url(self):
        return 'resources:resource_detail', (self.slug,)

    def __str__(self):
        return '%s - %s' % (self.name, self.link)


@python_2_unicode_compatible
class RelatedResources(models.Model):

    """Related items for primary item"""
    primary = models.ForeignKey(
        'resources.Resource',
        on_delete=models.CASCADE,
        related_name='primary_recommendations',
        verbose_name=_("Primary resource"))
    recommendation = models.ForeignKey(
        'resources.Resource',
        on_delete=models.CASCADE,
        verbose_name=_("Recomend resource"))
    ranking = models.PositiveSmallIntegerField(
        _('Ranking'), default=0,
        help_text=_('Determines order of the resource. A product with a higher'
                    ' value will appear before one with a lower ranking.'))

    class Meta:
        ordering = ['primary', '-ranking']
        unique_together = ('primary', 'recommendation')
        verbose_name = _('Product related')
        verbose_name_plural = _('Product related')


@python_2_unicode_compatible
class ProposeResource(models.Model):
    resource_name = models.CharField(_('Resource name'), max_length=100)
    category = models.ForeignKey('resources.Category', verbose_name=_('Category'))
    resource_url = models.URLField(_('Resource URL'))
    description = models.TextField(_('Description'))

    def __str__(self):
        return '%s - %s' % (self.resource_name, self.resource_url)