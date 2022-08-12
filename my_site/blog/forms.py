from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        labels = {
        'name' : 'Ваше имя',
        'e_mail' : "Введите ваш e-mail",
        'comment' : 'Комментарий'
        }