from django.db.models import Manager
from django.db.models import QuerySet
from application.choices import SubscriptionTypeChoices


class UserQuerySet(QuerySet):

    def get_free_users(self):
        return self.filter(type=SubscriptionTypeChoices.FREE)

    def get_advanced_users(self):
        return self.filter(type=SubscriptionTypeChoices.ADVANCED)

    def get_pro_users(self):
        return self.filter(type=SubscriptionTypeChoices.PRO)


class UserManager(Manager):

    def get_queryset(self):
        return UserQuerySet(self.model, using=self.db)

    def get_free_users(self):
        return self.get_queryset().get_free_users()

    def get_advanced_users(self):
        return self.get_queryset().get_advanced_users()

    def get_pro_users(self):
        return self.get_queryset().get_pro_users()
