from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Article


# Create your tests here.
class TestArticle(APITestCase):
    def test_api_article_list(self):
        url = reverse('api_articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
