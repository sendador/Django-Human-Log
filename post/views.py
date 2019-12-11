from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category


def index(request):
    queryset = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list': queryset
    }
    return render(request, 'index.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)

    context = {
        'post': post
    }
    return render(request, 'post.html', context)


def posts(request):
    queryset = Post.objects.order_by('-timestamp')[3:]
    context = {
        'object_list': queryset,
    }
    return render(request, 'posts.html', context)


def categories(request, cat):
    category_posts = Post.objects.all().filter(categories__title=cat)
    context = {
        'object_list': category_posts,
    }
    return render(request, 'posts.html', context)


def allPosts(request):
    queryset = Post.objects.order_by('-timestamp')
    context = {
        'object_list': queryset,
    }
    return render(request, 'posts.html', context)
