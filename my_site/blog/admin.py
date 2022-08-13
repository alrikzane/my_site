from turtle import title
from django.contrib import admin
from .models import Author, Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_display = ('author', 'title', 'date')
    list_filter = ('author', 'date', 'tag')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
