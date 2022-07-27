from datetime import date
from operator import pos


from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Author
all_posts = Post.objects.all().order_by("-date")
latest_posts = all_posts[:3]


def get_date(post):
    return post['date']


def index(request):
    return render(request, "blog/index.html", {
        'posts' : latest_posts
    })


def blog(request):
    return render(request, "blog/posts.html", {
        'blog' : all_posts
    })


def post(request, name):
    article = get_object_or_404(Post, slug=name)
    return render(request, "blog/article.html", {
        'article' : article,
        'tags' : article.tag.all()
    })
