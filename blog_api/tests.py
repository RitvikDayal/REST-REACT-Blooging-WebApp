from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User

class PostTests(APITestCase):

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def create_post(self):
        self.test_category = Category.objects.create(name='django')

        self.test_user_1 = User.objects.create(
            username='test_user_1',
            password='test_password'
        )

        data = {
            'title': 'New Title',
            'author': 1,
            'excerpt': 'New Title',
            'content':'New Content',
        }

        url = reverse('blog_api:listcreate')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

