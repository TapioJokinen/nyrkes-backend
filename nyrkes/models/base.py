from django.db import models


class BaseManager(models.Manager):
    pass


class BaseModel(models.Model):
    """Parent model for all models in this app."""

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = BaseManager()

    class Meta:
        abstract = True
