import django_filters

from performance_metrics.models import SampleDataset


class SampleDataFilter(django_filters.FilterSet):
    date = django_filters.DateFilter()
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    country = django_filters.CharFilter(lookup_expr='iexact')
    os = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = SampleDataset
        fields = ['date', 'channel', 'country', 'os']
