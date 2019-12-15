from django.test import TestCase, Client
from django.urls import reverse
from post.models import Category, Post


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category1 = Category.objects.create(title="Test")
        self.post1 = Post.objects.create(
            id=1,
            title='Post1',
            overview='Test',
            content='Test'
        )

    def test_index_GET(self):
        response = self.client.get(reverse('index_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_GET(self):
        response = self.client.get(reverse('post_detail', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post.html')

    def test_new_post(self):
        self.post1.categories.add(self.category1)
        for categories_list in self.post1.categories.all():
            categories_string = str(categories_list)

        self.assertEqual(self.post1.title, 'Post1')
        self.assertEqual(self.post1.overview, 'Test')
        self.assertEqual(self.post1.content, 'Test')
        self.assertEqual(categories_string, 'Test')
        self.assertEqual(self.post1.id, 1)

    def test_old_posts_GET(self):
        response = self.client.get(reverse('post_old'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')

    def test_categories_list_GET(self):
        response = self.client.get(
            reverse('categories_list', args=['some-categories']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')

    def test_add_new_categories(self):
        self.assertEqual(self.category1.title, 'Test')

    def test_all_posts_GET(self):
        response = self.client.get(reverse('post_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')
