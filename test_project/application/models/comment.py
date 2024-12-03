from django.db import models

from .abstract import TimeStampedModel


__all__ = ("Comment",)


class Comment(TimeStampedModel):
    content = models.TextField()
    post = models.ForeignKey("application.Post", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("application.User", on_delete=models.CASCADE, related_name="comments")
