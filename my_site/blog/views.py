from django.http import Http404
from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html")


def blog(request):
    return render(request, "blog/posts.html")


def post(request, name):
    return render(request, "blog/article.html", {
        'article' : 'cool article'
    })
