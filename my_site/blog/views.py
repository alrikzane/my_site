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
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            'article' : post,
            'tags' : post.tag.all(),
            'comment' : CommentForm(),
            'comments' : post.comments.all(),
            'is_saved_for_later' : self.is_stored_post(request, post.id)
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
            'comments' : post.comments.all(),
            'is_saved_for_later' : self.is_stored_post(request, post.id)
        }
        return render(request, "blog/article.html", context )


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts')
        context = {}
        if stored_posts is None or len(stored_posts)==0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        return render(request, 'blog/stored-posts.html', context)

    def post(self, request):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts = []
        id = int(request.POST['post_id'])
        if id not in stored_posts:
            stored_posts.append(id)
        else:
            stored_posts.remove(id)


        request.session['stored_posts'] = stored_posts
        return HttpResponseRedirect('/')
