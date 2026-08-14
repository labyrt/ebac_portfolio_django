from django.test import TestCase


class PostViewTest(TestCase):
    def test_post_view_returns_hello_world(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello World")
