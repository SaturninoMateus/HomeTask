import csv
import sys
from decimal import Decimal
from datetime import datetime

from django.core.management import BaseCommand
from django.core.management.base import OutputWrapper

from performance_metrics.models import SampleDataset


class ImportData:

    def __init__(self):
        self.stdout = OutputWrapper(sys.stdout)
        self.stderr = OutputWrapper(sys.stderr)

    def init_sampledataset(self, target_lists):
        """

        :param target_lists:
        :return:
        """

        self.stdout.write('Loading data...')
        for file in target_lists:
            self.stdout.write(f'file: {file}')

            with open(file) as f:
                reader = csv.reader(f)
                # skip header
                next(reader, None)
                for row in reader:
                    data = {
                        'date': datetime.strptime(row[0], '%d.%m.%Y').date(),
                        'channel': row[1],
                        'country': row[2],
                        'os': row[3],
                        'impressions': row[4],
                        'clicks': row[5],
                        'installs': row[6],
                        'spend': Decimal(str(row[7])),
                        'revenue': Decimal(str(row[8])),

                    }
                    SampleDataset.objects.update_or_create(**data)
        self.stdout.write('Done!')

class Command(BaseCommand):
    help = 'Import data from the sampledataset file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        ImportData().init_sampledataset(options['file'])
