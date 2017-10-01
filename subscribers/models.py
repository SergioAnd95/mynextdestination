from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from mailchimp3 import MailChimp

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        _('First name'),
        max_length=30,
        blank=True,
        null=True

    )
    last_name = models.CharField(
        _('Last name'),
        max_length=30,
        blank=True,
        null=True
    )
    mailchimp_id = models.CharField(
        _('Mailchimp id'),
        max_length=10,
        blank=True,
        null=True
    )

    def delete(self, using=None, keep_parents=False):
        m_id = self.mailchimp_id
        res = super().delete(using=using, keep_parents=keep_parents)
        if m_id and settings.MAILCHIMP_LIST_ID:
            client = MailChimp(settings.MAILCHIMP_LOGIN, settings.MAILCHIMP_API_KEY)
            try:
                client.lists.members.delete(settings.MAILCHIMP_LIST_ID, subscriber_hash=m_id)
            except Exception as info:
                pass

        return res


@receiver(post_save, sender=Subscriber)
def create_member_in_mailchimp(sender, instance=None, created=False, **kwargs):
    if created and settings.MAILCHIMP_LIST_ID:
        client = MailChimp(settings.MAILCHIMP_LOGIN, settings.MAILCHIMP_API_KEY)
        try:
            result = client.lists.members.create(settings.MAILCHIMP_LIST_ID, {'email_address': instance.email, 'status': 'subscribed'})
            instance.mailchimp_id = result['id']
            instance.save()
        except Exception as info:
           pass

