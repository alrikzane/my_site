from django.http import Http404
from django.shortcuts import render

def index(request):
    try:
        return render(request, "blog/index.html")
    except:
        raise Http404()

def blogposts(request):
    try:
        return render(request, "blog/posts.html")
    except:
        raise Http404()

def post(request, name):
    try:
        return render(request, "blog/post.html", {
            'post' : name
        })
    except:
        raise Http404()
