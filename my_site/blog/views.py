from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm

class index(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        query_set =  super().get_queryset()
        return query_set[:3]

class blog(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ['-date']
    context_object_name = 'blog'


class article(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            'article' : post,
            'tags' : post.tag.all(),
            'comment' : CommentForm(),
            'comments' : post.comments.all()
        }
        return render(request, "blog/article.html", context )

    def post(self, request, slug):
        comment = CommentForm(request.POST)        
        post = Post.objects.get(slug=slug)
        if comment.is_valid():
            comment_temp = comment.save(commit=False)
            comment_temp.post = post
            comment_temp.save()
            return HttpResponseRedirect(reverse('article', args=[slug]))              
        context = {
            'article' : post,
            'tags' : post.tag.all(),
            'comment' : comment,
            'comments' : post.comments.all()
        }
        return render(request, "blog/article.html", context )