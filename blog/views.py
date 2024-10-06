from django.shortcuts import render

posts = [
    {
        'author': 'Amith M',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 6, 2024',
    },
    {
        'author': 'Mihiranga A',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 4, 2024',
    },
    {
        'author': 'Madhavi P',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'October 1, 2024',
    },
]

def home(request):
    context = {
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')