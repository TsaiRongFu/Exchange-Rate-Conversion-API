import unittest
from flask import Flask
from main import app

class CurrencyConverterTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_conversion_success(self):
        response = self.app.get('/convert?source=USD&target=JPY&amount=$1,525')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['msg'], 'success')
        self.assertAlmostEqual(float(data['amount'][1:]), 170496.53, delta=0.02)

    def test_invalid_amount(self):
        response = self.app.get('/convert?source=USD&target=JPY&amount=invalid_amount')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'Invalid amount')

    def test_invalid_currency(self):
        response = self.app.get('/convert?source=EUR&target=JPY&amount=$1,525')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'Invalid currency')

if __name__ == '__main__':
    unittest.main()
