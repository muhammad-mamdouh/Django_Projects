from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from postings.models import BlogPost

User            = get_user_model()
payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler  = api_settings.JWT_ENCODE_HANDLER


class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfeuser', email='test@test.com')
        user.set_password('somerandopassword')
        user.save()
        blog_post = BlogPost.objects.create(
            user=user,
            title='New title',
            content='some_random_content'
        )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        posts_count = BlogPost.objects.count()
        self.assertEqual(posts_count, 1)

    def test_get_list(self):    # Test GET List
        data     = {}
        url      = api_reverse('api-postings:post-create-list', kwargs={'version': 'v1'})
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)

    def test_get_item(self):
        blog_post = BlogPost.objects.first()
        data      = {}
        url       = blog_post.get_api_url()
        response  = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_update_item(self):
        blog_post = BlogPost.objects.first()
        url       = blog_post.get_api_url()
        data      = {'title': 'Test POST title', 'content': 'Test POST content'}

        response  = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response  = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_item(self):
        data     = {'title': 'Test POST title', 'content': 'Test POST content'}
        url      = api_reverse('api-postings:post-create-list', kwargs={'version': 'v1'})
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_user(self):
        blog_post = BlogPost.objects.first()
        print(blog_post.content)
        url       = blog_post.get_api_url()
        data      = {'title': 'Test POST title', 'content': 'Test POST content'}
        user_obj  = User.objects.first()
        payload   = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)

        response  = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_post_item_with_user(self):
        data      = {'title': 'Test POST title', 'content': 'Test POST content'}
        url       = api_reverse('api-postings:post-create-list', kwargs={'version': 'v1'})
        user_obj  = User.objects.first()
        payload   = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)
        response  = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
