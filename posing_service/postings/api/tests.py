from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from postings.models import BlogPost

User = get_user_model()


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
