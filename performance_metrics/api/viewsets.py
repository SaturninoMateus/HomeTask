from django.db.models import Sum, Count, F, ExpressionWrapper, DecimalField
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response

from performance_metrics.api.filters import SampleDataFilter
from performance_metrics.api.serializers import SampledataSerializer
from performance_metrics.models import SampleDataset
from utils.utils import validate_fields


class SampledataViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = SampleDataset.objects.all()
    serializer_class = SampledataSerializer
    filterset_fields = ('date', 'channel', 'country', 'os')
    filterset_class = SampleDataFilter
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        """
        Retrieve all data
        Case the client send specify the group_by param
        (eg: /?group_by=os,country) the data will be grouped
        by the given columns, additionally, CPI will be calculated
        and added to the json object

        :return: a json with the requested data
        """

        group_by_fields = self.request.GET.get('group_by')

        if group_by_fields:
            group_by_fields = group_by_fields.split(',')
            validate_fields(group_by_fields, SampleDataset)
            self.queryset = self.queryset.values(*group_by_fields).order_by(
                *group_by_fields
            ).annotate(
                impressions=Sum('impressions'), clicks=Sum('clicks'),
                installs=Sum('installs'), spend=Sum('spend'),
                revenue=Sum('revenue'), count=Count('id')
            ).annotate(
                cpi=ExpressionWrapper(F('spend') / F('installs'),
                                      output_field=DecimalField()))
        # apply the filters
        qs = self.filter_queryset(self.queryset)
        data = self.serializer_class(qs, many=True,
                                     context={'request': request}).data
        return Response(data=data)
