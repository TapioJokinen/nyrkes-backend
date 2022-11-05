from django.db import models


class MenelManager(models.Manager):
    pass


class MenelModel(models.Model):
    """Parent model for all models in this app."""

    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = MenelManager()

    class Meta:
        abstract = True
