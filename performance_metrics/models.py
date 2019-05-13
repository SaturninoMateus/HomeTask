from django.core.validators import MinValueValidator
from django.db import models

from utils.models.dates import DatedModel


class SampleDataset(DatedModel):
    """
    A model that represents the SampleDataset
    """
    date = models.DateField()
    channel = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=10)
    impressions = models.BigIntegerField(default=0,
                                         validators=[MinValueValidator(0)])
    clicks = models.BigIntegerField(default=0,
                                    validators=[MinValueValidator(0)])
    installs = models.PositiveIntegerField(default=0)
    spend = models.DecimalField(max_digits=12, decimal_places=2)
    revenue = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.country + '-' + self.os + '-' + self.channel

    @classmethod
    def get_allowed_group_fields(self):
        """
        Return a list of fields that can be used
        query grouping
        :return:
        """
        return ['date', 'channel', 'country', 'os']
