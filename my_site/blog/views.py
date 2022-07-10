from django.http import Http404
from django.shortcuts import render

def index(request):

    return render(request, "blog/index.html", {
        'postlist' : [i for i in range(3)]
    })


def blog(request):
    try:
        return render(request, "blog/posts.html", {
            'postlist' : [i for i in range(3)]
        })
    except:
        raise Http404()

def post(request, name):
    try:
        return render(request, "blog/post.html", {
            'post' : name
        })
    except:
        raise Http404()
