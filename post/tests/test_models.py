from django.test import TestCase
from post.models import Post


class TestModels(TestCase):

    def setUp(self):
        self.post1 = Post.objects.create(
            id=1,
            title='Test'
        )

    def test__str__(self):
        self.assertEqual(str(self.post1), self.post1.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.post1.get_absolute_url(), '/post/1/')
