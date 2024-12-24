from django.db.models import Manager
from django.db.models import QuerySet
from application.choices import SubscriptionTypeChoices

class SubscriptionQuerySet(QuerySet):
    pass

class SubscriptionManager(Manager):

    def get_queryset(self):
        return SubscriptionQuerySet(self.model, using=self.db)


class FreeSubscriptionManager(SubscriptionManager):
    def get_queryset(self):
        return super().get_queryset().filter(type=SubscriptionTypeChoices.FREE)
