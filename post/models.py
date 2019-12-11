from django.db import models
from django.urls import reverse
from tinymce import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    content = HTMLField("Content")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
            'id': self.id
        })
