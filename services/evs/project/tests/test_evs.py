import json
import unittest

from project.tests.base import BaseTestCase
from project import db
from project.api.models import EV
# from project.api.models import Option


def add_ev(make, brand, ranges, base_price, storage, option_ids):
    ev = EV(make=make, brand=brand, ranges=ranges, base_price=base_price,
            storage=storage, option_ids=option_ids)
    db.session.add(ev)
    db.session.commit()
    return ev


class TestEvService(BaseTestCase):
    # Tests Electric Vehicle service

    def test_evs(self):
        # Ensure pinging route/function works
        response = self.client.get('/evs/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_ev(self):
        # Ensure a vehicle can be added by admin
        with self.client:
            response = self.client.post(
                '/',
                data=dict(make='Model 3', brand='Tesla', ranges=[],
                          base_price=35000, storage=15, option_ids=[]),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Electric Vehicles', response.data)
            self.assertNotIn(b'<p>No Electric Vehicles!</p>', response.data)
            self.assertIn(b'Model 3', response.data)

    def test_add_ev_invalid_json(self):
        # Ensure error is thrown when json is empty
        with self.client:
            response = self.client.post(
                '/evs',
                data=json.dumps({}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_ev_invalid_json_keys(self):
        # Ensure error is thrown if the json object does not have a make key
        with self.client:
            response = self.client.post(
                '/evs',
                data=json.dumps({
                    'make': 'Model 3'
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_ev_duplicate_make(self):
        # Ensure only one of each car make can be added
        with self.client:
            self.client.post(
                '/evs',
                data=json.dumps({
                    'make': 'Model 3',
                    'brand': 'Tesla',
                    'ranges': [],
                    'base_price': 35000,
                    'storage': 15,
                    'option_ids': []
                }),
                content_type='application/json'
            )
            response = self.client.post(
                '/evs',
                data=json.dumps({
                    'make': 'Model 3',
                    'brand': 'Tesla',
                    'ranges': [],
                    'base_price': 35000,
                    'storage': 15,
                    'option_ids': []
                }),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Sorry, this make already exists', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_ev(self):
        # Ensure getting a single EV works
        ev = add_ev('Model 3', 'Tesla', [], 35000, 15, [])
        with self.client:
            response = self.client.get(f'/evs/{ev.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('Model 3', data['data']['make'])
            self.assertIn('Tesla', data['data']['brand'])
            self.assertIn('success', data['status'])

    def test_single_ev_no_id(self):
        # Ensure error is thrown if an id is not provided
        with self.client:
            response = self.client.get(f'/evs/dog')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Vehicle does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_ev_incorrect_id(self):
        # Ensure error is thrown if the id does not exist
        with self.client:
            response = self.client.get(f'/evs/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Vehicle does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_evs(self):
        # Ensure we can get all vehicles in database
        add_ev('Model 3', 'Tesla', [], 35000, 15, [])
        add_ev('Model S', 'Tesla', [], 75000, 30, [])
        with self.client:
            response = self.client.get('/evs')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('success', data['status'])
            evs = data['data']['evs']
            self.assertEqual(len(evs), 2)
            self.assertIn('Model 3', evs[0]['make'])
            self.assertIn('Tesla', evs[0]['brand'])
            self.assertIn('Model S', evs[1]['make'])
            self.assertIn('Tesla', evs[1]['brand'])

    def test_main_no_evs(self):
        # Ensure main route works with no vehicles in the database
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Electric Vehicles', response.data)
            self.assertIn(b'<p>No Electric Vehicles!</p>', response.data)

    def test_main_with_evs(self):
        # Ensure main route works with vehicles in the database
        add_ev('Model 3', 'Tesla', [], 35000, 15, [])
        add_ev('Model S', 'Tesla', [], 75000, 30, [])
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Electric Vehicles', response.data)
            self.assertNotIn(b'<p>No Electric Vehicles!</p>', response.data)
            self.assertIn(b'Model 3', response.data)
            self.assertIn(b'Model S', response.data)


if __name__ == '__main__':
    unittest.main()
