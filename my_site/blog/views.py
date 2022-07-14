from datetime import date


from django.http import Http404
from django.shortcuts import render

postlist = [
    {
        'slug' : 'mountain-hike',
        'image' : 'mountains.jpg',
        'author' : "Алексей",
        'date' : date(2022, 7, 12),
        'title' : 'mountain hiking',
        'excerpt' : 'Нет ничего похожего на пейзажи, которые можно увидеть путешествуя по горам! Я не был готов к тому, что случилось, пока я наслаждался прекрасным видом...',
        'content' : """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias deleniti, error 
            ipsum dolorem tempora voluptas repellendus eum corrupti aperiam sit suscipit voluptatem doloremque, 
            tenetur ipsam dicta nobis quos non porro!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias deleniti, error 
            ipsum dolorem tempora voluptas repellendus eum corrupti aperiam sit suscipit voluptatem doloremque, 
            tenetur ipsam dicta nobis quos non porro!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias deleniti, error 
            ipsum dolorem tempora voluptas repellendus eum corrupti aperiam sit suscipit voluptatem doloremque, 
            tenetur ipsam dicta nobis quos non porro!
            """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Алексей",
        "date": date(2022, 6, 11),
        "title": "Программировать интересно!",
        "excerpt": "Вы когда-нибудь тратили часы на поиск одной мелкой ошбки в коде? Да, именно это и случилось со мной вчера...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Алексей",
        "date": date(2020, 8, 5),
        "title": "Природа во всей красе!",
        "excerpt": "Природа удивительна! Вдохновение, которое я получаю от прогулок на свежем воздухе удивительно.",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        'slug' : 'mountain-hike',
        'image' : 'mountains.jpg',
        'author' : "Алексей",
        'date' : date(2019, 7, 12),
        'title' : 'mountain hiking',
        'excerpt' : 'Нет ничего похожего на пейзажи, которые можно увидеть путешествуя по горам! Я не был готов к тому, что случилось, пока я наслаждался прекрасным видом...',
        'content' : """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias deleniti, error 
            ipsum dolorem tempora voluptas repellendus eum corrupti aperiam sit suscipit voluptatem doloremque, 
            tenetur ipsam dicta nobis quos non porro!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias deleniti, error 
            ipsum dolorem tempora voluptas repellendus eum corrupti aperiam sit suscipit voluptatem doloremque, 
            tenetur ipsam dicta nobis quos non porro!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias deleniti, error 
            ipsum dolorem tempora voluptas repellendus eum corrupti aperiam sit suscipit voluptatem doloremque, 
            tenetur ipsam dicta nobis quos non porro!
            """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Алексей",
        "date": date(2019, 6, 11),
        "title": "Программировать интересно!",
        "excerpt": "Вы когда-нибудь тратили часы на поиск одной мелкой ошбки в коде? Да, именно это и случилось со мной вчера...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Алексей",
        "date": date(2019, 8, 5),
        "title": "Природа во всей красе!",
        "excerpt": "Природа удивительна! Вдохновение, которое я получаю от прогулок на свежем воздухе удивительно.",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]
def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(postlist, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        'posts' : latest_posts
    })


def blog(request):
    return render(request, "blog/posts.html", {
        'blog' : postlist
    })


def post(request, name):
    article = next(post for post in postlist if post['slug'] == name)
    return render(request, "blog/article.html", {
        'article' : article
    })
