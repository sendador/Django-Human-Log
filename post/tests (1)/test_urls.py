from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hlog import urls
from post.views import index, post, posts, categories, allPosts


class TestUrls(SimpleTestCase):

    def test_index_page_url_resolves(self):
        url = reverse('index_page')
        self.assertEqual(resolve(url).func, index)

    def test_post_detail_url_resolves(self):
        url = reverse('post_detail', args=['1'])
        self.assertEqual(resolve(url).func, post)

    def test_old_post_url_resolves(self):
        url = reverse('post_old')
        self.assertEqual(resolve(url).func, posts)

    def test_categories_list_url_resolves(self):
        url = reverse('categories_list', args=['some-categories'])
        self.assertEqual(resolve(url).func, categories)

    def test_post_all_url_resolves(self):
        url = reverse('post_all')
        self.assertEqual(resolve(url).func, allPosts)
