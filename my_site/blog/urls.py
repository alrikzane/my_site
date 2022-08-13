from django.urls import path
from . import views


urlpatterns = [
    path("", views.index.as_view(), name = "index"),
    path('blog', views.blog.as_view(), name = "blog"),
    path('blog/<slug:slug>', views.article.as_view(), name = "article"),
    path('read-later', views.ReadLaterView.as_view(), name = 'read-later')
]