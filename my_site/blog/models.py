import email
from tkinter import CASCADE
from django.db import DatabaseError, models
from django.forms import CharField, DateField

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=35)
    e_mail = models.CharField(max_length=50)


class Tag(models.Model):
    caption = models.CharField(max_length=30)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    image_link = models.CharField(max_length=300)
    image_name = models.CharField(max_length=150)
    date = models.DateField()
    slug = models.SlugField()
    content = models.CharField(max_length=2000)






