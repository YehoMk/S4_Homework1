from django.db import models

from .abstract import TimeStampedModel
from application.managers.post import PostManager


__all__ = ("Post", )


class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey("application.User", on_delete=models.CASCADE, related_name="posts")  # Параметр on_delete вирішує, що буде з колонкою, якщо пов'язана колонка видаляється. model.CASCADE: Якщо видалиться user, то видаляться і пов'язані з ним пости. related_name="posts": user.posts дістане всі пов'язані пости

    objects = PostManager()  # Обираємо менеджер, який ми зробили. По замовчуваню є звичайнийй менеджер


Post.objects.filter_created_yesterday()
