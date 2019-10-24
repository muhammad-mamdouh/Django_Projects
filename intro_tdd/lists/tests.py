from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page(self):
        response = self.client.get('/')
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertIn('<title>To-Do Lists</title>', response.content.decode())
        self.assertTrue(
            response.content.decode().strip().endswith('</html>'),
            f"HTML did not end correctly. Was: {response.content}"
        )
        self.assertTemplateUsed(
            response, 'home.html',
            f'Unexpected template used other than home.html'
        )
