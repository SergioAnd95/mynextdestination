from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from taggit.managers import TaggableManager

from hitcount.models import HitCountMixin, HitCount

# Create your models here.


@python_2_unicode_compatible
class ResourceManager(models.Manager):
    def ordering_stage(self):
        return self.order_by('-priority', 'hit_count_generic__hits', '-when_created')


@python_2_unicode_compatible
class Category(models.Model):
    """
    Represent category
    """
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(_('Slug'))

    @permalink
    def get_absolute_url(self):
        return 'resources:category_detail', (self.slug, )

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Resource(models.Model, HitCountMixin):
    """
    Represent Resource
    """
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
    full_text = models.TextField(_('Text'))
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
    """Related resources for primary resource"""

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
    """
    Propose resources
    """
    resource_name = models.CharField(_('Resource name'), max_length=100)
    category = models.ForeignKey('resources.Category', verbose_name=_('Category'), blank=True, null=True)
    resource_url = models.URLField(_('Resource URL'))
    description = models.TextField(_('Description'), blank=True)
    when_created = models.DateTimeField(_('When created'), auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.resource_name, self.resource_url)


@receiver(post_save, sender=ProposeResource)
def send_notification(sender, instance=None, created=False, **kwargs):
    if created and settings.DEFAULT_FROM_EMAIL:
        # sending mails to all managers
        all_managers = User.objects.filter(is_superuser=True)
        if all_managers:
            managers_emails = [manager.email for manager in all_managers]
            subject = 'Send new propose for resource: %s' % (instance.resource_name)
            message = """
    Propose for resource:
    Resource Name: %s
    Resource URL:  %s
    Category:      %s
    Description:
    %s""" % (
                instance.resource_name,
                instance.resource_url,
                '' if not instance.category else instance.category.name,
                instance.description
            )
            send_mail(
                subject=subject,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=managers_emails,
                message=message
            )


