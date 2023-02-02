from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class APITests(TestCase):
        
    def setUp(self):
        self.client = APIClient()
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="password123")
        self.client.force_authenticate(admin_user)

    def testHealthGet(self):
        response = self.client.get('/symptom/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/diagnosis/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/food/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testHealthPost(self):
        response = self.client.post('/symptom/', {"symptom":"cough"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/diagnosis/', {"diagnosis":"IBS"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # can't post empty value
        response = self.client.post('/food/', {"food":""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post('/food/', {"food":"sugar"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)