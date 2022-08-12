import email
from django.db import models
from django.core.validators import MinLengthValidator

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    author = models.ForeignKey(Author,null=True, on_delete=models.SET_NULL, related_name="posts")
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'images', null = True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    

class Comment(models.Model):
    name = models.CharField(max_length=30)
    e_mail = models.EmailField(null=True)
    comment = models.TextField(max_length=400)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name='comments')





