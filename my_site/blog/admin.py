from turtle import title
from django.contrib import admin
from .models import Author, Tag, Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    list_display = ('author', 'title', 'date')
    list_filter = ('author', 'date', 'tag')



admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
