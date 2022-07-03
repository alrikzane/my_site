from django.urls import path
from . import views


urlpatterns = {
    path('', views.index, name = "inex"),
    path('blog', views.blogposts, name = "posts"),
    path('blog/<slug:name>', views.post, name = "post")
}