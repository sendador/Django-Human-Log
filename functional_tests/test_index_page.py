from selenium import webdriver
from post.models import Post
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestPostListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'functional_tests\geckodriver.exe')

    def tearDown(self):
        self.browser.quit()

    def test_redirect_to_old_posts(self):
        self.browser.get(self.live_server_url)
        old_posts_url = self.live_server_url + reverse('post_old')
        self.browser.find_element_by_id('old-post').click()
        self.assertEqual(self.browser.current_url, old_posts_url)

    def test_redirect_to_all(self):
        self.browser.get(self.live_server_url)
        all_posts_url = self.live_server_url + reverse('post_all')
        self.browser.find_element_by_id('all-posts').click()
        self.assertEqual(self.browser.current_url, all_posts_url)

    def test_user_can_see_post(self):
        post1 = Post.objects.create(
            title='Post1',
            overview='Test Overview',
        )
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.find_element_by_class_name('post-title').text, 'Post1')

    def test_contact_text_swap(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('contact').click()
        self.assertEqual(self.browser.find_element_by_id('text').text, 'kamil.ulfik@gmail.com')

