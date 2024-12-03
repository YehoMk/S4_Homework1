from django.db import models


__all__ = ("Subscription",)


class Subscription(models.Model):
    user = models.OneToOneField("application.User", on_delete=models.CASCADE, related_name="subscription")
    type = models.CharField(max_length=100, choices=(("free", "Free"), ("advanced", "Advanced"), ("pro", "Pro")))
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.IntegerField()
    is_active = models.BooleanField(default=False)
