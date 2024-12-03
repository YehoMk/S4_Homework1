import datetime

from django.db.models import Manager
from django.db.models import F, Value, CharField
# F = Field
from django.db.models.functions import Concat
from django.db.models import QuerySet

from datetime import timedelta


class PostQuerySet(QuerySet):  # PostQuerySet. В ньоу функцї. Це для того, щоб ми могли виконувати методи над QuerySetами

    def with_user_info(self):
        return self.annotate(user_info=Concat(F('user__username'), Value(" ("), F('user__email'), Value(")"), output_field=CharField()))  # Додаємо до кожного рядка поста додатковий рядок, який є ім'ям пов'язаного з постом користувача

    def filter_created_yesterday(self):
        return self.filter(created_at=datetime.datetime.now() - timedelta(days=1))


class PostManager(Manager):

    def get_queryset(self):  # Підвязуємо до менеджера PostQuerySet
        return PostQuerySet(self.model, using=self._db)

    def filter_created_yesterday(self):
        return self.get_queryset().filter_created_yesterday()
