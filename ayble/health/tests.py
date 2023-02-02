from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status

class APITests(TestCase):
        
    def setUp(self):
        self.client = APIClient()

    def testHealthGet(self):
        response = self.client.get('/symptom/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/diagnosis/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/food/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)