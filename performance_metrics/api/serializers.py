from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from performance_metrics.models import SampleDataset


class SampledataSerializer(ModelSerializer):
    """
    A serializer for SampleDataset model
    """
    cpi = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        """
        Dynamically change the fields to be shown
        according to the request
        """
        # @TODO Optimize this -_-'
        super(SampledataSerializer, self).__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('group_by')
        if fields:
            fields = fields.split(',')
            fields += ['impressions', 'clicks', 'installs', 'spend', 'revenue',
                       'cpi', 'id']
            # Drop any fields that are nt specified in the `group_by` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())

            for f in existing - allowed:
                self.fields.pop(f)

    class Meta:
        model = SampleDataset
        fields = (
            'id', 'date', 'channel', 'country', 'os', 'impressions',
            'clicks', 'installs', 'spend', 'revenue', 'cpi')

    def get_cpi(self, obj):
        try:
            return obj.get('cpi')
        except:
            return

    def to_representation(self, obj):
        ret = super(SampledataSerializer, self).to_representation(obj)
        # no need to show the CPI in this case
        if not ret['cpi']:
            ret.pop('cpi')
        return ret
