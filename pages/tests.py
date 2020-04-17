from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    
    def test_home_page_reference_name(self):
        request = self.client.get(reverse('home'))
        self.assertEqual(request.status_code, 200)

    def test_home_page_content(self):
        request = self.client.get(reverse('home'))
        self.assertContains(request, 'Hello World')
        
