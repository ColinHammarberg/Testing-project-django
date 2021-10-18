from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OrderLineItem

# Saving order total


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.total_order()
