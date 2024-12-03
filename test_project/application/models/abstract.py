from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Буде додаватись один раз при створенні
    updated_at = models.DateTimeField(auto_now=True)  # Буде додаватись кожен раз при оновлені об'єкта

    class Meta:
        abstract = True
