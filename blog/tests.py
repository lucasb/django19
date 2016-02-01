from django.test import TestCase, RequestFactory

from .views import post_detail

# Create your tests here.
class BlogTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_post_detail(self):
        request = self.factory.get('/post/1')
        response = post_detail(request)
        self.assertEqual(response.status_code, 200)
