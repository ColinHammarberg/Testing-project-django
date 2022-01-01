from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=50, null=True, blank=False)
    default_email = models.EmailField(max_length=254, null=True, blank=False)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=False)
    default_street_address = models.CharField(
        max_length=80, null=True, blank=False)
    default_postcode = models.CharField(max_length=20, null=True, blank=False)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=False)
    default_county = models.CharField(max_length=80, null=True, blank=False)
    default_country = CountryField(
        blank_label='Country', null=True, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserAccount.objects.create(user=instance)
    # Existing users: just save the profile
    instance.useraccount.save()