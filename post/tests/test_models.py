from django.test import TestCase, Client
from post.models import Category, Post


class TestModels(TestCase):

    def setUp(self):
        post1 = Post.objects.create(title='Test')

    def test__str__(self):
        post1 = Post.objects.get(id=1)
        self.assertEqual(str(post1), post1.title)

    def test_get_absolute_url(self):
        post1 = Post.objects.get(id=1)
        self.assertEqual(post1.get_absolute_url(), '/post/1/')
