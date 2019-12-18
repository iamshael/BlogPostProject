from django.shortcuts import render

posts = [
    {
        'author': 'Shailesh Akarte',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 16, 2019'
    },
    {
        'author': 'Dhnyanada Mendhe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 17, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)


def about(request):
    return render(request, 'blogapp/about.html', {'title': 'About'})
