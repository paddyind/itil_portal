import os
from django.test import TestCase, Client
from unittest import mock

class HealthCheckTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @mock.patch.dict(os.environ, {"DB_ENGINE": "django.db.backends.sqlite3", "DB_NAME": ":memory:"})
    def test_health_check(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
