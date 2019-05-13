from rest_framework.test import APITestCase

# @TODO change to namespace and reverse
URL = '/api/sampledata/'


class TestFilter(APITestCase):
    fixtures = ['tests_data.json']

    def setUp(self) -> None:
        self.url = URL

    def test_filter_by_date(self):
        params = {'date': '2017-05-17'}
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(2, len(response.data))

    def test_filter_by_date_from_and_date_to(self):
        date_from = '2017-05-17'
        date_to = '2017-05-18'
        params = {'date_from': date_from,
                  'date_to': date_to}
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(2, len(response.data))

    def test_filter_by_os(self):
        params = {
            'os': 'android'
        }
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(2, len(response.data))
        params['os'] = 'android'
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(2, len(response.data))

    def test_filter_by_channel(self):
        params = {
            'channel': 'facebook'
        }
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(2, len(response.data))
        self.assertEqual('facebook', response.data[0]['channel'])
        self.assertEqual('facebook', response.data[1]['channel'])

    def test_filter_by_country(self):
        params = {
            'country': 'MT'
        }
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(1, len(response.data))
        self.assertEqual('MT', response.data[0]['country'])


class TestGroupColumns(APITestCase):
    fixtures = ['tests_data.json']

    def setUp(self) -> None:
        self.url = URL

    def test_groupby_channel(self):
        params = {
            'group_by': 'channel'
        }
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(2, len(response.data))
        self.assertEqual('adcolony', response.data[0]['channel'])
        self.assertEqual(33773, response.data[0]['impressions'])
        self.assertEqual(830, response.data[0]['clicks'])

        self.assertEqual('facebook', response.data[1]['channel'])
        self.assertEqual(6615, response.data[1]['impressions'])
        self.assertEqual(196, response.data[1]['clicks'])

    def test_groupby_channel_and_os(self):
        params = {
            'group_by': 'channel,os'
        }
        response = self.client.get(self.url, format='json', data=params)
        self.assertEqual(4, len(response.data))
        self.assertEqual('adcolony', response.data[0]['channel'])
        self.assertEqual(19887, response.data[0]['impressions'])
        self.assertEqual(494, response.data[0]['clicks'])

        self.assertEqual('adcolony', response.data[1]['channel'])
        self.assertEqual(13886, response.data[1]['impressions'])
        self.assertEqual(336, response.data[1]['clicks'])

        self.assertEqual('facebook', response.data[2]['channel'])
        self.assertEqual(3237, response.data[2]['impressions'])
        self.assertEqual(125, response.data[2]['clicks'])

        self.assertEqual('facebook', response.data[3]['channel'])
        self.assertEqual(3378, response.data[3]['impressions'])
        self.assertEqual(71, response.data[3]['clicks'])

# @TODO: Add test cases for CPI calculation and ordering