
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()