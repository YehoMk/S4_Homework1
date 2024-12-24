from django.db import models
from django.utils import timezone

from application.choices import SubscriptionTypeChoices
from application.models import User
from application.managers.subscription import FreeSubscriptionManager

__all__ = ("Subscription",)


class Subscription(models.Model):
    user = models.OneToOneField("application.User", on_delete=models.CASCADE, related_name="subscription")
    type = models.CharField(max_length=100, choices=SubscriptionTypeChoices.choices)
    start_date = models.DateField(timezone.now(), null=True)
    end_date = models.DateField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)


class FreeSubscribtion(Subscription):
    class Meta:
        proxy = True

    objects = FreeSubscriptionManager
