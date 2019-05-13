from django.db import models
from django.db.models import Count
from unixtimestampfield import UnixTimeStampField
Count

class RecordsQuerySet(models.QuerySet):
    """
    QS that helps to separate deleted records from present
    in all inherited models.
    """

    def present(self):
        return self.filter(deleted=False)

    def deleted(self):
        return self.filter(deleted=True)


class DatedModel(models.Model):
    created_at = UnixTimeStampField(auto_now_add=True, use_numeric=True)
    updated_at = UnixTimeStampField(auto_now_add=True, auto_now=True, use_numeric=True)
    deleted = models.BooleanField(default=False)

    objects = RecordsQuerySet.as_manager()

    class Meta:
        abstract = True
        ordering = ('id',)
