from django.test import TestCase

# Create your tests here.

class HelloEndpointTests(TestCase):
    def test_hello_endpoint_returns_success(self):
        response = self.client.get("/api/hello/")
        self.assertEqual(response.status_code, 200)

    def test_hello_endpoint_returns_expected_course(self):
        response = self.client.get("/api/hello/")
        self.assertEqual(response.json()["course"], "CSC325")
