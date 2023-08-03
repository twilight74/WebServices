import json
import requests
import unittest


class TestWeb(unittest.TestCase):
    # initializing the variables
    data = {"name": "test1", "number": "01"}
    django_url = "http://django:7000/home/"
    flask_url = "http://flask:8000/home/"
    fastapi_url = "http://fastapi:3000/home/"
    django_response = requests.post(django_url, json=data)
    flask_response = requests.post(flask_url, json=data)
    fastapi_response = requests.post(fastapi_url, json=data)

    def test_status_code(self):
        # assertion for response data and status code and
        self.assertEqual(self.django_response.status_code, self.flask_response.status_code)
        self.assertEqual(self.flask_response.status_code, self.fastapi_response.status_code)

    def test_server(self):
        # assertion for server
        self.assertEqual(self.django_response.headers.get("server"), self.flask_response.headers.get("server"))
        self.assertEqual(self.flask_response.headers.get("server"), self.fastapi_response.headers.get("server"))

    def test_date(self):
        # assertion for date
        self.assertEqual(self.django_response.headers.get("date"), self.flask_response.headers.get("date"))
        self.assertEqual(self.flask_response.headers.get("date"), self.fastapi_response.headers.get("date"))

    def test_header_component(self):
        # assertion for all components of headers
        for key in self.django_response.headers:
            self.assertEqual(self.django_response.headers[key], self.flask_response.headers[key])
            self.assertEqual(self.flask_response.headers[key], self.fastapi_response.headers[key])
